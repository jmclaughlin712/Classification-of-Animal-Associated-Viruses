# Classification of Animal Associated Viruses

![image](https://github.com/jmclaughlin712/Classification-of-Animal-Associated-Viruses/assets/126025563/31a5e689-4d9a-4217-8a5f-60038e50b24d)



 ### **Business Problem**

This project aims to classify the animal associated with a zoonotic virus based on its DNA and protein sequences. Knowing the source of a virus is critical for identifying emerging diseases, preventing future outbreaks, faster vaccine development, and protecting ecosystems. Most pandemics throughout history have been zoonotic in nature, and 3 out of every 4 emerging infectious diseases are spread from animals to humans. 

 ### **Data Overview**

The data in this project comes from ZOVER- http://www.mgc.ac.cn/cgi-bin/ZOVER/main.cgi. The ZOVER database contains over 60,000 viruses and their corresponding genetic sequences. The data has been collected from all over the world, and the sequences were obstracted from animal tissue, cells, and feces. All the viruses are associated with one of four animals: either bats, rodents, mosquitos, or ticks. 

 ### **Data Limitations**

The data was limited to viruses associated with those 4 animals, and did not for example contain any viruses associated with birds or larger mammals. Some of the sequences were only partial sequences, which is why there were duplicates in the data. The data did not contain any numeric values, so I had to use feature engineering to create a dataset that was suitable for models.  

 ### **Data Exploration**

After importing necessary packages and reading in the data, I constructed a dataframe of about 50,000 rows (once duplicates were removed). Each row represents a unique virus, and contains a label identifying the animal it is associated with. Each row also contains the DNA sequence for the virus, as well as its corresponding proteins. Some of the viruses have many associated proteins. I explored the data to see the typical length of the DNA sequences. The vast majority were under 10,000 characters long but there were some sequences with as many as 30,000 characters. I also looked at the distribution of viruses by associated animal, and found that bats are the majority class with about 15,000 associated viruses, and ticks are the fewest with about 8,000. Rodents have around 13,000 viruses and Mosquitos have about 12,000. I did not feel this was a stark enough difference to use SMOTE. 

 ### **Feature Engineering**

My approach to creating numeric data was to identify patterns of occurrences within the sequences. For DNA sequences, I looked at patterns of 5, 6, 7,and 8 letters and created binary columns representing whether the sequence contained that pattern or not. Since there is an extremely large number of possible patterns that can occur (4^x, with x being the number of letters in the pattern), I took a random sample of patterns for each respective length. I did the same for protein sequences except I looked at lengths of 1 and 3 only. Each time the notebook is ran, the dataset has different columns. Even with random sampling, the run time for the whole notebook is still close to an hour. 

 ### **Preprocessing**

My preprocessing steps were scaling the data and label encoding the target.

### **Statistical Significance**

I checked the training data to see which columns have statistically significant differences between bats, rodents, mosquitos, and ticks. I used an ANOVA test for this. Columns which are not statistically significant will be dropped. This turns out to be less than 1% of the columns, so the vast majority of columns are statistically significant.

 ### **Modeling**

As mentioned, my final model is a voting classifier which combines the predictions of XGBoost models and neural networks. The classifier makes its predictions based on a simple majority vote. It iterates through each potential combination of models to find the one that optimizes accuracy based on the given dataset. I had to create a function for the classifier - I was not able to use sklearn's built in Voting Classifier object because XGBoost models and neural networks require different dimensions for the arrays containing the target labels. XGBoost requires one dimensional arrays and neural networks require n dimensional arrays, with n being the number of target classes (4 in this case). However the final result is the same as if I had used a Voting Classifier object with uniform weights. The XGBoost models each had a different max_depth in the range 10-15, which I found to be the optimal size for performance. The neural networks utilized dense layers with 'relu' activation functions, and the output layers used 'softmax' activation functions since the project is a multilevel classification problem. To reduce overfitting I also included dropout and batch normalization layers after each dense layer, and applied L2 regularization. I created one larger neural network wth 4 hidden layers and two smaller networks with 1 hidden layer each. I created 5 XGBoost models, for a total of 8 models. I used label binarization to evaluate my final model's ROC-AUC score. 

 ### **Results**

The final model has an accuracy score of about 95.4% and a precision-recall curve with inflection point close to 1. Therefore the model is effective at identifying the associated animal species of viruses.
