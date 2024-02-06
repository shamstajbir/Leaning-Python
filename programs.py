import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import skew

# Load the dataset
file_path = "//Users/shamstajbirtonmoy/Downloads/Diabetes.csv"
df = pd.read_csv(file_path)

# Display the first and last 5 rows, and data types
print(df.head(5))
print(df.tail(5))
print(df.dtypes)

# Drop 'DiabetesPedigreeFunction' column
df.drop(['DiabetesPedigreeFunction'], axis=1, inplace=True)

# Rename columns
df.rename(columns={"BloodPressure": "BP", "SkinThickness": "SkinThick"}, inplace=True)

# Display shape and size
print(df.shape)
print(df.size)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Display count and check for missing values
print(df.count())
print(df.isnull().sum())

# Drop rows with missing values
df.dropna(inplace=True)

# Display count and check for missing values again
print(df.count())
print(df.isnull().sum())

# Boxplots and outlier removal
plt.figure(figsize=(10, 6))
sns.boxplot(x='BP', data=df)
plt.title("Boxplot for Blood Pressure")
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='BMI', data=df)
plt.title("Boxplot for BMI")
plt.show()

# Outlier removal using IQR
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
df = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]

# Display shape after outlier removal
print(df.shape)

# Bar plot for age distribution
plt.figure(figsize=(10, 6))
df.Age.value_counts().nlargest(40).plot(kind='bar')
plt.title("Number of persons age-wise")
plt.ylabel('Persons')
plt.xlabel('Age')
plt.show()

# Correlation matrix
print(df.corr())

# Outcome distribution
print(df['Outcome'].value_counts())

# Min and max values for each column
for col in df.columns:
    print("The minimum value for the column {} is {}".format(col, df[col].min()))
    print("The maximum value for the column {} is {}".format(col, df[col].max()))

# Skewness for each feature
for col in df.drop('Outcome', axis=1).columns:
    print("Skewness for the column {} is {}".format(col, skew(df[col])))
