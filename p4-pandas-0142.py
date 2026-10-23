import pandas as pd 
import numpy as np
# yahir sifuentes  NC 0142 
n_filas=5
n_columnas=5
tag_columna=tuple("ABCDE") # etiquetas para las columnas 
print(tag_columna)
matriz=np.random.randint(1,6, size=(n_filas, n_columnas))
print("genera matriz de 5 filas por 5 columnas")
print("con numeros comprendios entre 1 y 6")
print(matriz)
# la variable df es DataFrame
df = pd.DataFrame(matriz, columns= tag_columna )
print("--- la tabla o DataFrame ---- NC= 0142")
print(" yahir sifuentes NC = 0142 ")



