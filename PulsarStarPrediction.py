# Create the DataFrames for both the train and test datasets and store them in the 'train_df' and 'test_df' variables respectively.
import pandas as pd
train_df = pd.read_csv('https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/project-5/pulsar-star-prediction-train.csv')
test_df = pd.read_csv('https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/project-5/pulsar-star-prediction-test.csv')

# Display the first 5 rows of the 'train_df' DataFrame.
train_df.head()

# Display the first 5 rows of the 'test_df' DataFrame.
test_df.head()

# Display the last 5 rows of the 'train_df' DataFrame.
train_df.tail()

# Display the last 5 rows of the 'test_df' DataFrame.
test_df.tail()

# Print the number of rows and columns in both the DataFrames.
print(train_df.shape)
test_df.shape

# Check for the missing values in the 'train_df' DataFrame.
train_df.isnull()

# Check for the missing values in the 'test_df' DataFrame.
test_df.isnull()

# Print the count of the '0' and '1' classes in the 'train_df' DataFrame.
train_df['target_class'].value_counts()

# Print the count of the '0' and '1' classes in the 'test_df' DataFrame.
test_df['target_class'].value_counts()

# Get the feature variables from the 'train_df' DataFrame.
x_train = train_df.iloc[ : , 1:]
# Display the first 5 rows of the 'x_train' DataFrame.
x_train.head()

# Get the feature variables from the 'test_df' DataFrame.
x_test = test_df.iloc[: , 1:]
# Display the first 5 rows of the 'x_test' DataFrame.
x_test.head()

# Get the target variable from the 'train_df' DataFrame.
y_train = train_df['target_class']
# Display the first 5 rows of the 'y_train' Pandas series.
y_train.head()

# Get the target variable from the 'test_df' DataFrame.
y_test = test_df['target_class']
# Display the first 5 rows of the 'y_test' Pandas series.
y_test.head()

# Build A XGBoost Classifier model
# Import the xgboost module.
import xgboost as xg
# Import the confusion_matrix and classification_report modules.
from sklearn.metrics import confusion_matrix, classification_report
xgb_clf =xg.XGBClassifier()
xgb_clf.fit(x_train, y_train)

# Predict the target variable based on the feature variables of the test dataframe.
y_pred = xgb_clf.predict(x_test)
print(y_pred)

# Print the confusion matrix to see the number of TN, FN, TP and FP.
cm = confusion_matrix(y_test, y_pred)
cm

# Print the precision, recall and f1-score values for both the '0' and '1' classes.
print(classification_report(y_test, y_pred))
