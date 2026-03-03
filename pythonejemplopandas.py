#Necesita la libreria de panda
import pandas as pd
#Las series se van a llamar

datos = {
    'Nombres' : ['Ana','Adian','Lucia','Antonia'],
    'Edad' : [23,25,12,40],
    'Ciudades':['Madrid', 'Sevilla','Toledo','Gijon']
}

#Estas series de datos se almacenas en objetos llamados Data frame de las librerias Pandas
df = pd.DataFrame(datos)
print(df)
#Podemos filtrar los datos si lo deseaos
#df[df['Dato] = > valor]
print("---------Data Frame filtrado---------")
deffiltrado = df[df['Edad'] >24 ]
print(deffiltrado)
print("--------Data Frame Ordenado-----")
dforden= df.sort_values("Edad")
print(dforden)

