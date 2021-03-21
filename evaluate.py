
import os 

def main():

    print("Working On It")

    trueP = 0
    falseN = 0
    falseP = 0
    trueN = 0

    
    datacounter = 0
    dataLi = []
    restDat = []

    confusionMat = []
    totalItem = 0
    classes = ["soft", "hard", "none"]

    for i in range(len(classes)):
        confusionMat.append([0,0,0])


    with open ("fulldata.txt", 'r') as f:
        for line in f:
          

            if line.startswith("@attribute"):
                restDat.append(line)

            elif line.startswith("@data"):
                restDat.append(line)
                datacounter = 1

            elif (datacounter == 1):
                dataLi.append(line)

    

    for i in range(len(dataLi)):
        test = open("test.arff", "w")
        train = open("train.arff", "w")

        for l in restDat:
            test.write(l)
            train.write(l)
      
        testing = dataLi[i]
        
        prev = dataLi[:i]
        after = dataLi[i + 1:]
        copyList = prev + after

    
        curcheck = testing.split(",")
        aType = curcheck[-1]
        actualType = aType[:-1]
        test.write(testing)
        
        for x in range(len(copyList)):

            train.write(copyList[x])

        train.close()
        test.close()

        os.system('python3 naivebayes.py train.arff test.arff resulting.txt')


        predictedType = ""

        with open ("resulting.txt", 'r') as f:
            for line in f:
                line = line.rstrip()
                if line.startswith("Final"):
                    
                    lin = line.split(": ")
                    pType = lin[-1]
                    predictedType = pType
        
        #print(str(actualType) + " | " + str(predictedType))
                    
        if (str(actualType) == str(predictedType)):
            
            clasi = classes.index(actualType)
    
            confusionMat[clasi][clasi] += 1
            totalItem = totalItem + 1
        
        else:

            clasi1 = classes.index(actualType)
            clasi2 = classes.index(predictedType)
            confusionMat[clasi1][clasi2] += 1
            totalItem = totalItem + 1



    correctVal = 0

    for i in range(len(confusionMat)):
        #print(confusionMat[i][i])

        correctVal = correctVal + confusionMat[i][i]  

    overallAcc = correctVal / totalItem
    #print(overallAcc)

    outi = open("evaluation.txt", "w")

    outi.write("Confusion Matrix & Overall Accuracy" + "\n" + "\n")



    for i in range (len(confusionMat)):
        if (i == 0):
            outi.write("    soft  hard  none" + "\n")
        line = classes[i] + " "
        for j in range(len(confusionMat[i])):
            
            line = line + str(confusionMat[i][j]) + "      "
        
        outi.write(line + "\n" )

    outi.write("\nOverall Accuracy: " + str(overallAcc))

    outi.close()

    print("Done")


if __name__ == "__main__":
    main()