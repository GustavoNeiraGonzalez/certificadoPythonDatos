# -*- coding: utf-8 -*-
import pandas as pd
"""
Si los datos llegaran a ser impresos en notación
científica, puedes desactivar la notacion cientifica con 
este comando: set_option(...) antes de leerlo con read_
"""
pd.set_option( 'display.float_format', lambda x:'%.5f' % x)

casen = pd.read_csv("casen_2017.csv",sep=";", encoding="unicode_escape")

"""
podemos usar describe con una columna especifica:
"""

casen["edad"].describe()
"""
Este resumen nos dice que hay 216.439 personas que
reportan su edad; la edad promedio es de 37.8 años,
con una desviación estándar de 22.95, donde la edad
mínima es de 0 años, y la máxima de 117, con una
mediana de ingreso de 36 años ¿Te da esto una idea de
cómo podrían estar distribuidas las edades en el país?
Por ejemplo, sabemos que el 50% de la muestra tiene
36 años o menos, y el 50% restante edades superiores a
ese número. Pero vemos que el promedio de edades es
un poco más alto, situándose en 38 aproximadamente
¿por qué crees que podría ocurrir esto?
Por último nos indica el tipo de datos que es esta
variable, un float.
--
si queremos recuperar las edades distintas dentra de la tabla con .nunique()
es decir si en [18, 18, 20, 25, 25, 25, 30], el resultado es 4 porque hay 4 edades unicas (18 20 25 30)
"""
casen["edad"].nunique()

"""
tambien podemos recuperar la edad maxima
"""
casen["edad"].max()
"""
tambien podemos agrupar los datos en este ejemplo sacando el promedio de edad por sexos
"""
casen.groupby("sexo")["edad"].mean()
"""
Si quisiéramos asignar esto a un objeto en formato dataframe para analizarlo aparte y visualizar la tabla,
incluimos el parámetro "as_index=False", de esta forma:
"""
edad_por_sexo = casen.groupby("sexo", as_index=False)["edad"].mean()
"""----- agregar a hombres y mujeres indigenas ---
creamos una columna para hombres y mujeres indigenas a modo de muestra creamos una columna 
    que usaremos para agregarlos, esta columna cuenta a cada persona
    """
casen["contador"] = 1
"""
Con esto, vamos a proceder a agregar. Para ello, los dataframe poseen una función que les permite agregar
distintas columnas dentro de los datos, esta es .groupby(), "agrupar por", la cual funciona así:
    
casen.groupby(["sexo", "es_indigena"]) no hace nada

Como vemos, esta función por sí sola no hace nada, solo crea un objeto de tipo dataframe, que tiene datos
para ser agregados. Para volverlo un elemento comprensible, debemos especificar "qué" es lo que estamos
agregando por cada grupo, su ingreso, su edad, su cantidad, u otro. Nosotros estamos agregando su
cantidad, esto es, cuanta gente hay por cada grupo.

Para esto, junto con .groupby() debemos especificar otra función de agregación, entre ellas existe una que
se conoce como .agg() de "aggregate", y se invoca así:
"""
casen.groupby(["sexo", "es_indigena"]).agg()
""" ---ERROR---
no obstante nos da error
esto es porque aun no proporcionamos datos
PARA AGREGAR Lo siguiente:
    donde "sum" La operación que queremos aplicar a esta variable. Esto implica
        que pueden aplicarse otras fórmulas como un promedio."""
casen.groupby(["sexo", "es_indigena"]).agg({"contador":"sum"})
"""
ahora finalmente hemos contado la gente que es y no es indigena diferenciada por sexo
"""
"""
Siguiendo esta lógica, podemos aplicar otras operaciones a cualquier va lor numérico dentro de nuestros
datos. Por ejemplo, si en vez de contar, quisiéramos sacar el promedio de ingreso, lo podemos hacer de esta
forma (recuerda que "mean" = promedio).
"""
casen.groupby(["sexo", "es_indigena"]).agg({"ingreso":"mean"})

"""luego estos datos los podemos asignar a una variable y podremos visualizar la tabla  
    por etnicidad y sexo
    """

etnicidad_y_sexo = casen.groupby(["sexo", "es_indigena"]).agg({"contador":"sum"})
"""
para calcular un porcentaje o de hombres indigenas o mujeres indigenas es ejemplo hombre indigenas:
    333110
    ------
    (333110+517780) = hombres indigenas
    esto es indigenasHombres/(indigenasHombres/NoIndigenasHombres)
"""
"""
ahora implementemos estos porcentajes en python """

etnicidad_y_sexo.groupby("sexo").sum()
"""
En este caso, lo que queremos es el
total de personas por cada sexo, lo cual se obtiene en el ejemplo de arriba

luego finalmente sacamos los porcentajes:"""

etnicidad_y_sexo /etnicidad_y_sexo.groupby("sexo").sum()

"""
aqui vemos los porcentajes de no y si indigenas mujeres y hombres
"""






