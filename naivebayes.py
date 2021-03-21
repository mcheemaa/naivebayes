
import numpy as np
import sys




def input(fileName):
    
    clas = []
    priors = []
    datadict = {}
    featureList = []

    datacounter = 0

    with open (fileName, 'r') as f:
        
        for line in f:
            
            line = line.rstrip()
            

            if line.startswith("@attribute"):

                splitline = line.split()
                datadict [splitline[1]] = []
                featureList.append(splitline[1])

           
                for i in range(2, len(splitline)):
                    temp = splitline[i]
                    final = ""

                    if (i == 2):
                        final = temp[1:-1]
                    else:
                        final = temp[:-1]

                    (datadict[splitline[1]]).append(final)

            elif line.startswith("@data"):
                datacounter = 1

            elif (datacounter == 1):

                splitline = line.split(',')

                tempList = []

                for i in range(len(splitline)):
                    

                    item = splitline[i]

                    feNum = (datadict[featureList[i]]).index(item)
                    
                    

                    if (i == len(splitline) - 1):

                        clas.append(feNum)

                    else:
                        tempList.append(feNum)

                priors.append(tempList)       
    
    pri = np.array(priors) 
    cl = np.array(clas)


    
    return pri, cl, datadict, featureList

    

def calcPrior (outcome):
    
    examples = len(outcome)
    uni = np.unique(outcome)

    final = {}

    countr = []

    for i in range(len(uni)):
        counter = 0
        for j in range(len(outcome)):
            if (uni[i] == outcome[j]):
                counter = counter + 1

        if (counter == 0):
            counter = 1  

        countr.append(counter)


    for i in range(len(uni)):

        final[uni[i]] = countr[i] / (examples)

    for i in uni:
        row_indices = np.where(outcome == i)[0]

    return final




def naiveB (pri, cl, test):
    
    classes = np.unique(cl)
    attr = np.unique(pri)
    rows, cols = np.shape(pri)


    likely = {}
    likely_prob = {}

    for cls in classes:
        likely[cls] = []
        likely_prob[cls] = []

    classProb = calcPrior(cl)


    match = []

    for i in classes:
        temp = []
        for j in range(len(cl)):

            if (i == cl[j]):
                temp.append(j)

        match.append(temp)



    for i in range (len(classes)):
        
        numR = match[i]

        for j in range(len(numR)):

            for x in range(cols):

                if (len(likely[i]) < cols):
                    likely[i].append([])
                    
                (likely[i][x]).append(pri[numR[j]][x])




    for i in range (len(classes)):
        
        for x in range(cols):
            if (len(likely_prob[i]) < cols):
                    likely_prob[i].append({})

            likely_prob[i][x] = calcPrior(likely[i][x])


    result = []

    
    for j in range(len(test)):
        results = {}
        for i in classes:

            classP = classProb[i]

            for x in range(len(test[j])):

                val = likely_prob[i][x]
                
                if test[j][x] in val.keys():
                    classP *= val[test[j][x]]
                else:
                    classP *= 0
                    

            results[i] = classP
        result.append(results)
    
    return(result)


def output(filename, result, datadict, pri2, feat):

    file1 = open(filename, "w")
    file1.write("Contact Lense Type\n" + "\n")

    typee = ""
    for y in range (len(feat)-1):
        typee = typee + feat[y] + " | "


    file1.write("Data In Type: " + typee + "\n" + "\n" )

    for i in range(len(pri2)):
        fin = ""
        for j in range(len(pri2[i])):
            att = feat[j]
            
            fin = fin + datadict[att][pri2[i][j]] + " | "

        dat = result[i]
        newFin = ""
        tempLit = []    
        att = feat[-1]
        tempLi = []

        for x in dat.keys():
            res = result[i]
            pro = res[x]
            tempLi.append(pro)

        su = sum(tempLi)

        for x in dat.keys():
            res = result[i]
            probi = res[x]/su
            tempLit.append(probi)

            newFin = newFin + datadict[att][x] + ": " + str(probi) + " " 
        
        maxi = max(tempLit)
        indi = tempLit.index(maxi)

        predi = datadict[att][indi] 

        fin = fin + "\n"
        file1.write("Data In: " + fin)
        file1.write("Lense Class Probs: " + newFin + "\n")
        file1.write("Final Class: " + predi + "\n")
        file1.write("\n")  
    file1.close()  





def main():

    pri, cl, datadict, featuree = input(sys.argv[1])
    pri2, cl2, datadict2, featureee = input(sys.argv[2])
    test_sample = np.array((0,0,0,1))
    result = naiveB(pri, cl, pri2)

    output(sys.argv[3], result, datadict, pri2, featuree)


    

    

if __name__ == "__main__":
    main()


