import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('./dataset/World Wide Cases detail.csv', encoding='latin1')

df = df.drop_duplicates()
if df['Iso3_code'].isnull().sum() > 0:
    df['Iso3_code'] = df['Iso3_code'].fillna(df['Iso3_code'].mean())

df['Year'] = pd.to_datetime(df['Year'], format='%Y')
df['Category'] = df['Category'].astype('category')

scaler = MinMaxScaler()
# df[['Country']] = scaler.fit_transform(df[['Country']])

df = pd.get_dummies(df, columns=['Category'])

df.to_csv('./dataset/World Wide Cases detail_cleaned.csv', index=False)