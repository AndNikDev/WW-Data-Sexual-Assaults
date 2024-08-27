import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Cargar el dataset
df = pd.read_csv('./dataset/World Wide Cases detail.csv', encoding='latin1')

# Verificar si el DataFrame se ha cargado correctamente
if df.empty:
    print('Error: Data Frame is empty')
else:
    print('Data Frame loaded successfully')

# Eliminar duplicados
df = df.drop_duplicates()

# Verificación de valores nulos y manejo
for column in ['Iso3_code', 'Country', 'Region', 'Subregion', 'Indicator', 'Dimension', 'Sex', 'Age', 'Year', 'Unit of measurement', 'VALUE']:
    if df[column].isnull().sum() > 0:
        if df[column].dtype == 'object':  # Si es categórico, llenamos con la moda (valor más frecuente)
            df[column] = df[column].fillna(df[column].mode()[0])
        else:  # Si es numérico, llenamos con la media
            df[column] = df[column].fillna(df[column].mean())

# Conversión de la columna 'Year' a datetime
df['Category'] = df['Category'].astype('category')
df = pd.get_dummies(df, columns=['Category'])

# Verificar y eliminar filas con fechas inválidas en 'Year'
# df = df.dropna(subset=['Year'])

# Escalado de la columna 'VALUE' si existe y tiene datos válidos
if 'VALUE' in df.columns and not df['VALUE'].isnull().all():
    scaler = MinMaxScaler()
    df[['VALUE']] = scaler.fit_transform(df[['VALUE']])
else:
    print("La columna 'VALUE' no existe o está vacía.")

# Codificación de variables categóricas en 'Category'
# Nota: No se incluye ya que 'Category' no está presente en las columnas originales que mencionaste

# Eliminación de columnas irrelevantes (si es necesario)
columns_to_drop = ['Source']  # Ejemplo de columna a eliminar si no es relevante
df = df.drop(columns=columns_to_drop, axis=1)

# Guardar el dataset limpio
df.to_csv('./dataset/World Wide Cases detail_cleaned.csv', index=False)

# Mostrar la información del DataFrame para verificar
print(df.info())
print(df.head())

df_cleaned = pd.read_csv('./dataset/World Wide Cases detail_cleaned.csv')
df_cleaned.to_json('./dataset/cleaned_data.json', orient='records')

