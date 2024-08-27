import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('./dataset/World Wide Cases detail.csv', encoding='latin1')

if df.empty:
    print('Error: Data Frame is empty')
else:
    print('Data Frame loaded successfully')

df = df.drop_duplicates()

for column in ['Iso3_code', 'Country', 'Region', 'Subregion', 'Indicator', 'Dimension', 'Sex', 'Age', 'Year', 'Unit of measurement', 'VALUE']:
    if df[column].isnull().sum() > 0:
        if df[column].dtype == 'object':
            df[column] = df[column].fillna(df[column].mode()[0])
        else: 
            df[column] = df[column].fillna(df[column].mean())

df['Category'] = df['Category'].astype('category')
df = pd.get_dummies(df, columns=['Category'])

if 'VALUE' in df.columns and not df['VALUE'].isnull().all():
    scaler = MinMaxScaler()
    df[['VALUE']] = scaler.fit_transform(df[['VALUE']])
else:
    print("The column 'VALUE' don't exist or is empty")

df.to_csv('./dataset/World Wide Cases detail_cleaned.csv', index=False)

print(df.info())
print(df.head())

df_cleaned = pd.read_csv('./dataset/World Wide Cases detail_cleaned.csv')
df_cleaned.to_json('./dataset/cleaned_data.json', orient='records')

