
import pandas as pd
import numpy as np

diabetes_data = pd.read_csv('diabetes.csv')

# INITIAL INSPECTION
# check variable types
print(diabetes_data.dtypes)

# check data
print(diabetes_data.head())

# how many rows (observations) the data contain
print(diabetes_data.shape)

# columns in the data which have null (missing) values
print(diabetes_data.isnull().sum())
print(diabetes_data.info())

# calculate summary statistics of the data
print(diabetes_data.describe())
# the 'minimum' summary stats is 0, which makes no sence
# also outliers are observed in 'Pregnancies' and 'Insulin' columns

diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.nan)

# check null values again
print(diabetes_data.isnull().sum())
print(diabetes_data.info())

# Print out all of the rows that contain missing (null) values
print(diabetes_data[diabetes_data.isnull().any(axis=1)])

# check data variables types
print(diabetes_data.dtypes)

# 'Outcome' variables datatype
print(diabetes_data.Outcome.unique())

# fix misentries data in 'Outcome'
diabetes_data['Outcome'] = diabetes_data['Outcome'].replace('O', '0')
print(diabetes_data.Outcome.unique())

# change Outcome dtype to 'int64'
diabetes_data['Outcome'] = diabetes_data['Outcome'].astype('int64')
print(diabetes_data.dtypes)
