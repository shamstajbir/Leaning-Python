import pandas as pd
import numpy as np
df = pd.read_csv("/Volumes/ERAM/machine learning/lab3/DataPreprocessing.csv")
df.head()
df.isnull().sum()
df.dtypes
df.info()
df.head()


np.unique(df['MSSubClass'])
np.unique(df['LotConfig'])

np.unique(df['HouseStyle'])

df.replace([':-', '?', '__', '_', '#', "##", 'Na', 'Nan'], np.nan, inplace = True)

df.head()
df.isnull().sum()

df['MSSubClass'].fillna(int(df['MSSubClass'].mode()), inplace=True)


df['LotFrontage'].fillna(int(df['LotFrontage'].mode()), inplace=True)

df['BldgType'].fillna('1Fam', inplace=True)
df['HouseStyle'].fillna('1Story', inplace=True)
df['OverallQual'].fillna(int(df['OverallQual'].mode()), inplace=True)
df['OverallCond'].fillna(int(df['OverallCond'].mode()), inplace=True)

df['RoofStyle'].fillna('Gable', inplace=True)
df['TotalBsmtSF'].fillna(int(df['TotalBsmtSF'].mean()), inplace=True)

df['BedroomAbvGr'].fillna(int(df['BedroomAbvGr'].mode()), inplace=True)
df['GarageArea'].fillna(int(df['GarageArea'].mean()), inplace=True)
df.isnull().sum()
df.info()
df['LotFrontage']=df['LotFrontage'].astype('int64')
df['OverallQual']=df['OverallQual'].astype('int64')

df['OverallCond']=df['OverallCond'].astype('int64')
df['BedroomAbvGr']=df['BedroomAbvGr'].astype('int64')

from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()

df['LotConfig'] = label_encoder.fit_transform(df['LotConfig'])
df['Neighborhood'] = label_encoder.fit_transform(df['Neighborhood'])

df['BldgType'] = label_encoder.fit_transform(df['BldgType'])
df['HouseStyle'] = label_encoder.fit_transform(df['HouseStyle'])
df['RoofStyle'] = label_encoder.fit_transform(df['RoofStyle'])
df.head()
df.info()
df.to_excel('AfterPreprocssing1.xlsx')
df.head()

from datetime import date
df.insert(11, "House_Age", date.today().year - df['YearBuilt'])

df['LotArea'] = df['LotArea'].apply(lambda x: 10*round(x/10))

df.head()
Min = df['LotArea'].min()
Max = df['LotArea'].max()
df['LotArea'] = df['LotArea'].apply(lambda x: ((x-Min)*40/(Max-Min))+10)
df['LotArea'] = df['LotArea'].apply(np.floor)
Mean = np.round(df['LotFrontage'].mean())

Std = df['LotFrontage'].std()

df['LotFrontage'] = df['LotFrontage'].apply(lambda x: ((x-Mean)/Std))
Maximum = df['TotalBsmtSF'].max()
digits = len(str(Maximum))
Abs = pow(10,digits)

df['TotalBsmtSF'] = df['TotalBsmtSF'].apply(lambda x: (x/Abs))

df.head()