import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset.
beng_csv = "https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/bengaluru-house-prices/Bengaluru_House_Prices.csv"
beng_df = pd.read_csv(beng_csv) 
beng_df.head()

# Display the number of rows and columns.
beng_df.shape

# Find the total number of missing values in each column.
beng_df.isnull().sum()

# Find the percentage of missing values
beng_df.isnull().sum() * 100 / beng_df.shape[0]

# Get all the rows having the missing values in the 'location'.
beng_df.loc[beng_df['location'].isnull() == True, :]

# Total number of rows having the missing values in the 'location' column.
beng_df.loc[beng_df['location'].isnull() == True, :].shape[0]

# Discard the rows containing the missing values in the 'location' column.
beng_df = beng_df.loc[beng_df['location'].isnull() == False, :]
beng_df

# Get the rows having the missing values in the 'size' column.
beng_df.loc[beng_df['size'].isnull() == True, :]

# Total number of rows having the missing values in the 'size' column.
beng_df.loc[beng_df['size'].isnull() == True, :].shape[0]

# Discard the rows containing the missing values in the 'size' column.
beng_df = beng_df.loc[beng_df['size'].isnull() == False, :]
beng_df

# Get the rows having the missing values in the 'total_sqft' column.
beng_df.loc[beng_df['total_sqft'].isnull() == True, :]

# Get the rows having more than 5 bathrooms in the 'bath' column.
beng_df[beng_df['bath'] > 5]

# Get the rows having the missing values in the 'total_sqft' column.
beng_df.loc[beng_df['total_sqft'].isnull() == True, :]

# Get the rows having more than 5 bathrooms in the 'bath' column.
beng_df[beng_df['bath'] > 5]

# Discard the rows having more than 5 bathrooms in the 'bath' column.
beng_df = beng_df[beng_df['bath'] <= 5]
beng_df

# Percentage of missing values.
beng_df.isnull().sum() * 100 / beng_df.shape[0]

# List of the columns to be retained.   
cols_to_keep = []
for col in beng_df.columns:
  if col != 'society':
    cols_to_keep.append(col)

cols_to_keep

# Retain the appropriate columns in the DataFrame.
beng_df = beng_df.loc[:, cols_to_keep]
beng_df.head()

# Retain the appropriate columns in the DataFrame.
beng_df = beng_df.loc[:, cols_to_keep]
beng_df.head()