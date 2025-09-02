import pandas as pd

casen = pd.read_csv("casen_2017.csv", sep=";",encoding='unicode_escape')
casen = pd.read_csv("casen_2017.csv", sep="/")

"""
La función ".read_csv()" recibe 3 parámetros: el nombre del archivo que queremos importar, el símbolo que
separa los datos dentro de ese archivo (sep=";") y la encodificación.

La encodificación es un tema muy sensible y puede ser un verdadero dolor de cabeza. Esta define la forma en que
el computador procesa diversos caracteres tales como letras, números, pero también símbolos o recursos
ortográficos, como las tildes, tildes invertidas, letras en otros lenguajes o símbolos no textuales,
tales como:     "#","&","~" entre otros.

En general, la encodificación por defecto está basada en el inglés, por lo que caracteres que contienen tildes
pueden dar problemas. En este caso especificamos una encodificación que permite procesar escritura latina en
general.
"""

casen
""" ya con casen podemos imprimir los datos de el archivo .csv (este tipo de archivos es para gran
cantidad de datos)
"""
casen.head(3)
"""
con .head() podemos imprimir las primeras filas en este caso las 3 primeras
tambien desde explorador de variables en la parte derecha dando doble click en dataframe
, se podra ver una perspectiva mas general de los datos 
"""
casen.sexo
casen["sexo"]
"""
de estas 2 formas podemos buscar los mismos datos de la columna sexo
"""
casen.sexo[10]
casen["sexo"].iloc[10]
"""
de estas 2 formas obtendriamos la fila 10
pero iloc puede ser mas especifica ya que:
    si tuvieramos un data frame llamado datos de 4 columnas y 4 filas para recuperar el valor
    de la fila 3 columna 2 se haria:
        iloc.[3,2]
        el 3 es fila y el 2 columna
"""

casen.loc[casen["sexo"]=="Mujer"]
"""
Otra forma de manipular los datos es filtrando, por ejemplo, obteniendo columnas con características
específicas. Si quisiéramos filtrar solo a las mujeres del dataframe seria como el ejemplo de arriba
"""
casen.loc[(casen["sexo"]=="Mujer") & (casen["esc"]>12)]
"""
También podemos hacer consultas más complejas, como por ejemplo, filtrar a todas las mujeres con
más de 12 años de escolaridad, para lo cual usaremos operadores lógicos. Aunque se ven distintos de
los operadores booleanos de Python, tienen la misma lógica, donde and es "&" y or es "l"
"""
casen.iloc[10,3]
"""
También podemos buscar datos en las tablas por
coordenadas, como el número de fila y columna,
por ejemplo, si queremos recuperar Ia fila 10 de Ia
columna 3, lo podemos hacer en el ejemplo de arriba
 """
casen.iloc[:,[2, 5, 6]] 
"""
O podemos recuperar ciertas columnas o filas
específicas, en este caso, recuperaremos la
columna 25 6:
    
El símbolo de dos puntos ":" en la posición de las
filas de Ia propiedad .iloc[], indica "todos", esto es,
tráeme "todas las filas" de las columnas 2, 5 y 6.
"""
casen["mayorA18"] = casen.edad > 18
casen["mayorA18"]

"""
con casen["mayorA18"] = casen.edad >18 
estamos creando otra columna llamada mayorA18 donde se verifica si es mayor de edad o no
guardandolo como true o false
"""
casen.describe()
"""
Junto con constatar que es lo que tiene el dataframe, también podemos obtener
algunos estadísticos descriptivos para hacernos la idea de la distribución de los datos con la funcion
.describe()

Esto nos da algunas métricas que hemos visto en las sesiones anteriores corno el promedio, la desviación
estándar, o los respectivos cuantiles, entre ellos Ia mediana 
"""