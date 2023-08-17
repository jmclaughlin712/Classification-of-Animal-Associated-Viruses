**Business Problem**
This project aims to classify the animal associated with a zoonotic virus based on its DNA and protein sequences. Knowing the source of a virus is critical for identifying emerging diseases, preventing future outbreaks, faster vaccine development, and protecting ecosystems. Most pandemics throughout history have been zoonotic in nature, and 3 out of every 4 emerging infectious diseases are spread from animals to humans. 

**Data Overview**
The data in this project comes from ZOVER- http://www.mgc.ac.cn/cgi-bin/ZOVER/main.cgi. The ZOVER database contains over 60,000 viruses and their corresponding genetic sequences. The data has been collected from all over the world, and the sequences were obstracted from animal tissue, cells, and feces. All the viruses are associated with one of four animals: either bats, rodents, mosquitos, or ticks. 

**Data Limitations**
The data was limited to viruses associated with those 4 animals, and did not for example contain any viruses associated with birds or larger mammals. Some of the sequences were only partial sequences, which is why there were duplicates in the data. The data did not contain any numeric values, so I had to use feature engineering to create a dataset that was suitable for models.  

**Data Exploration**
After importing necessary packages and reading in the data, I constructed a dataframe of about 50,000 rows (once duplicates were removed). Each row represents a unique virus, and contains a label identifying the animal it is associated with. Each row also contains the DNA sequence for the virus, as well as its corresponding proteins. Some of the viruses have many associated proteins. I explored the data to see the typical length of the DNA sequences. The vast majority were under 10,000 characters long but there were some sequences with as many as 30,000 characters. I also looked at the distribution of viruses by associated animal, and found that bats are the majority class with about 15,000 associated viruses, and ticks are the fewest with about 8,000. Rodents have around 13,000 viruses and Mosquitos have about 12,000. I did not feel this was a stark enough difference to use SMOTE. 

**Feature Engineering**
My approach to creating numeric data was to identify patterns of occurrences within the sequences. For DNA sequences, I looked at patterns of 5, 6, 7,and 8 letters and created binary columns representing whether the sequence contained that pattern or not. Since there is an extremely large number of possible patterns that can occur (4^n, with n being the number of letters in the pattern), I took a random sample of patterns for each respective length. Even with random sampling, the run time for the whole notebook is still close to an hour. 
