#The credit card clients dataset is full of irregularities and incorrect values. You need to replace them with the right values. Additionally, you have to create box plots, count plots and histograms to find a specific trend (if there exists) in the dataset.

# Import the modules.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset.
# Dataset link: 'https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/uci-credit-card-fraud/UCI_Credit_Card.csv'
dataset_101 = pd.read_csv('https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/uci-credit-card-fraud/UCI_Credit_Card.csv')
dataset_101.head()

# Number of rows and columns using the 'shape' function.
dataset_101.shape

# Check for the missing values by using the 'sum()' function on top of the 'isnull()' function.
dataset_101.isnull().sum()

# Counts of each value in the 'EDUCATION' column. 
dataset_101['EDUCATION'].value_counts()

# Replace the unwanted values in the 'EDUCATION' column. Ignore if there are none.
dataset_101.loc[dataset_101['EDUCATION']==0 , 'EDUCATION']=5
dataset_101.loc[dataset_101['EDUCATION'] == 6, 'EDUCATION'] = 5 
dataset_101['EDUCATION'].value_counts()

# Percentage of each value in the 'EDUCATION' column
dataset_101['EDUCATION'].value_counts() * 100 / dataset_101.shape[0]

# Count plot for the 'EDUCATION' column using the 'countplot()' function of 'seaborn' module.
plt.figure(figsize=(20,5))
kp1=sns.countplot(x='EDUCATION' , data=dataset_101)
for p in kp1.patches:
  kp1.annotate(p.get_height(), xy = (p.get_x() + p.get_width()/2 , p.get_height()) , ha='center' , va='bottom')
plt.grid()
plt.show()

# Check the data-types of all the columns using the 'info()' function.
dataset_101.info()

# Counts of each value in the 'MARRIAGE' column.
dataset_101['MARRIAGE'].value_counts()

# Replace the unwanted values ('0') in the 'MARRIAGE' column with '3'. Ignore if there are none.
dataset_101.loc[dataset_101['MARRIAGE'] ==0 , 'MARRIAGE'] = 5
dataset_101.loc[dataset_101['MARRIAGE'] ==3 , 'MARRIAGE'] = 5
dataset_101['MARRIAGE'].value_counts()

# Percentage of the values in the 'MARRIAGE' column.
dataset_101['MARRIAGE'].value_counts() *100/ dataset_101.shape[0]

# Count plot for the 'MARRIAGE' column.
plt.figure(figsize=(20,5))
kp2=sns.countplot(x='MARRIAGE' , data=dataset_101)
for k in kp2.patches:
  kp2.annotate(k.get_height() , xy=(k.get_x() + k.get_width()/2 , k.get_height()), ha='center' , va='bottom')
plt.grid()
plt.show()

# Box plot for the 'AGE' column using the 'boxplot()' function.
plt.figure(figsize=(20,5))
sns.boxplot(dataset_101['AGE'])
plt.show()

# Histogram for the 'AGE' column using 'distplot()' function from the 'seaborn' module.
plt.figure(figsize=(20,5))
kp3 = plt.hist(dataset_101['AGE'] , bins=12)
for u in kp3[2]:
  plt.annotate(u.get_height() , xy=(u.get_x() + u.get_width()/2 , u.get_height()) , ha='center' , va='bottom')
plt.grid()
plt.show()

# Box plot for the LIMIT_BAL column.
plt.figure(figsize=(20,5))
sns.boxplot(dataset_101['LIMIT_BAL'])
plt.show()

# Histogram for the 'LIMIT_BAL' column using 'distplot()' function from the 'seaborn' module.
plt.figure(figsize=(20,5))
kp4=sns.distplot(dataset_101['LIMIT_BAL'] , kde=False)
for r in kp4.patches:
  kp4.annotate(r.get_height() , xy=(r.get_x() + r.get_width()/2 , r.get_height()) , ha='center' , va='bottom')
plt.grid()
plt.show()

# Histogram (having 50 bins) for the 'LIMIT_BAL' column using 'hist()' function from the 'matplotlib.pyplot' module.
plt.figure(figsize=(20,5))
kp5=plt.hist(dataset_101['LIMIT_BAL'] , bins=50)
for b in kp5[2]:
  plt.annotate(b.get_height() , xy=(b.get_x() + b.get_width()/2 , b.get_height()) , ha='center' , va='bottom')
plt.grid()
plt.show()





































