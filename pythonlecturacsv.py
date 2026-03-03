import pandas as pd
#. vamos a ver datos de nuestro csv
#Creamos un data frame a partir del fichero
df = pd.read_csv('data/datos.csv',delimiter=';')
#printeamos dataframe
print(df)
#podemos indicar el numero de filas
print("Primeras 5 filas")
print(df.head(7))
#Podemos conveertir los datos en diccionarios 
#Para Trabajar con python puro.abs
print("-------------------------------")
diccionario = df.to_dict(orient='records')
print(diccionario)
print("-------------------------------")
for registro in diccionario:
    print (registro)
print("-------------------------------")
#podemos hacer cálculos, por ejemplo la media
df_media= df['edad'].mean()
print(df_media)
print("-------------------------------")
df_grupo = df.groupby('ocupacion')
print(df_grupo.size())
print("-------------------------------")

