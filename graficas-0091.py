import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
print("Numero de lista = 25")
print("Christian Garcia Jimenez Nc = 0091")
print("Fecha = lunes/11/Noviembre/19/2026 ")

# crearemos nuestra tabla y la guardaremos con pandas
# Tenemos 5 listas de ecommerce con 4 elementos por lista
amz = ['Amazon', 310, True, 1994]
ali = ['Aliexpress', 150, True, 2010]
ml  = ['Mercado Libre', 108, True, 1999]
ebg = ['eBay', 133, False, 1995]
shk = ['Shopee', 200, True, 2015]

# Creamos una lista de listas (conformando la tabla)
lista_ecommerce = [amz, ali, ml, ebg, shk]
# print(lista_ecommerce)

# Utilizar pandas para utilizar la tabla (dataframe o marco de datos)
# A cada columna la ponemos nombre
df_ecommerce = pd.DataFrame(lista_ecommerce, columns=["nombre", "cantidad", "es_fa", "año"])
print(df_ecommerce)

# Crear el archivo CSV y lo guarda en CSV
# df_ecommerce.to_csv("ecommerce.CSV", index=False)

# Crear grafica de lineas 
# Donde x es nombre en el eje horizontal
# Donde y es cantidad en el eje vertical
plt.plot(df_ecommerce["nombre"], df_ecommerce["cantidad"])
plt.title(" Grafica de ecommerce  Nc = 0091")
plt.xlabel("Nombre de ecommerce")
plt.ylabel("Cantidad de usuarios")
plt.show()

# Creamos una grafica de puntos 
plt.scatter(df_ecommerce["nombre"], df_ecommerce["cantidad"])
plt.title("Ecommerce 0091")
plt.xlabel("Las tiendas")
plt.ylabel("cantidad de usuarios")
plt.show()

# Generar la gráfica de barras
plt.bar(df_ecommerce["nombre"], df_ecommerce["cantidad"])
# Personalización con título y etiquetas
plt.title("Ecommerce 0091")
plt.xlabel("Las tiendas")
plt.ylabel("cantidad de usuarios")
# Mostrar la gráfica con paréntesis ()
plt.show()

# Ordenar Grafica de barras de manera desendente 
# De la mas grande a la pequeña
df_ecom_ordenar = df_ecommerce.sort_values("cantidad", ascending = False)
plt.bar(df_ecom_ordenar["nombre"], df_ecom_ordenar["cantidad"])
plt.title("Ecommerce 0091")
plt.xlabel("Las tiendas")
plt.ylabel("cantidad de usuarios")
plt.show()

# Coloreado la grafica
plt.bar(df_ecom_ordenar["nombre"], df_ecom_ordenar["cantidad"],
        color = ["b", "g", "c", "m", "y"])
plt.title("Ecommerce 0091")
plt.xlabel("Las tiendas")
plt.ylabel("cantidad de usuarios")
plt.show()

# Grafica de pastel
# plt.pie(df_ecom_ordenar["nombre"], df_ecom_ordenar["cantidad"],
plt.pie(df_ecom_ordenar["cantidad"], labels = df_ecom_ordenar["nombre"])
plt.title("Ecommerce 0091")
plt.xlabel("Las tiendas")
plt.ylabel("cantidad de usuarios")
plt.show()