# Naive Bayes Algorithm

In this naivebayes.py  trains a Naive Bayes classifier from a training file and makes predictions on an input file which contains independent data samples with the same set of features. For example, runs using the provided sample files (sampletraining.arff and sampleinput.arff) as below: $python3 naivebayes.py sampletraining.arff sampleinput.arff predictions.txt. 



# Confusion Matrix & Overall Accuracy

    soft  hard  none
soft 4      0      1      
hard 0      1      3      
none 1      2      12      

Overall Accuracy: 0.7083333333333334


# Results 

Contact Lense Type


Data In Type: age | spectacle-prescrip | astigmatism | tear-prod-rate 


Data In: pre-presbyopic | hypermetrope | no | reduced 

Lense Class Probs: soft: 0.0 hard: 0.0 none: 1.0 

Final Class: none



Data In: young | hypermetrope | no | reduced 

Lense Class Probs: soft: 0.0 hard: 0.0 none: 1.0 
Final Class: none




Data In: pre-presbyopic | myope | yes | normal 

Lense Class Probs: soft: 0.0 hard: 0.0 none: 1.0 

Final Class: none



Data In: pre-presbyopic | hypermetrope | no | normal 

Lense Class Probs: soft: 0.7531710661638669 hard: 0.0 none: 0.24682893383613302 

Final Class: soft



Data In: young | myope | yes | normal 

Lense Class Probs: soft: 0.0 hard: 0.6854914196567862 none: 0.31450858034321383 

Final Class: hard






