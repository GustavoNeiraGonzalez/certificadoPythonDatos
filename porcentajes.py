# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 15:27:16 2025

@author: tavo-
"""

"""---porcentajes-----"""

x = 1500 * 0.15
x
import pandas as pd

grupoA = [50,40]
""" esos 2 arrays son ['no recompensados', 'recompensados']"""
grupoB = [60,70]

datos = {"Grupo A":grupoA,"Grupo B":grupoB}

"""usaremos nombreFilas Para ponerle nombre a las filas dentro de la tabla que veremos con el dataframe"""
nombreFilas = ["Sin recompensa","Con recompensa"]
"""
Luego, podemos usar el parámetro index de la función
".DataFrame()" de la librería pandas (a la que le asignamos el
alias pd), para agregarle estos nombres a nuestro dataframe, así:
"""
tabla = pd.DataFrame(datos,
                     index=nombreFilas)
tabla
"""--haciendo porcentajes--
primero necesitamos de esta tabla obtener totales usando sum()"""
tabla.sum()
"""total de personas """
totalPersonas = sum(tabla.sum())
totalPersonas
"""
Hecho esto, para obtener el total de personas sin recompensa, lo que hacemos es indicar por medio del
comando .loc[ ] el nombre o número de la fila que queremos recuperar.
"""
tabla.loc["Sin recompensa"] 
""" pero para sumarlos todos los sin recompensa:"""
totalSinRecompensa = sum(tabla.loc["Sin recompensa"])
totalSinRecompensa
"""Finalmente con estos 2 valores, calculamos el porcentaje."""
(totalSinRecompensa/totalPersonas)*100
""" el resultado es 50, ahora sabemos que el total de personas sin recompensa es el 50%"""

"""---LOC NOS PERMITE EXPLORAR EL DATAFRAME CON ESTA LOGICA ->
dataframe.loc[ 'nanbre o número de fila', 'nombre o número de COLUMNA']
asi obtenemos un valor especifico de la tabla 
"""

"""aunque los porcentajes pueden ser engañosos ya que """
(tabla.loc["Con recompensa", "Grupo B"]/totalPersonas)*100
"""31.8%"""
(tabla.loc["Con recompensa", "Grupo A"]/totalPersonas)*100
"""18.18%"""
(tabla.loc["Sin recompensa", "Grupo B"]/totalSinRecompensa)*100
""" 54.5%"""
"""
el grupo B puede decir que son menos recompensados ya que el 55% no recibe recompensa en total de no recompensados
mientras A puede decir que b son mas numerosos y B tienen mas recompensas en comparacion al TOTAL de personas 
aqui el porcentajes de los 2 grupos no recompensados en TOTAL DE PERSONAS
"""
(tabla.loc[ "Sin recompensa"]/ tabla.sum())*100


"""----LEY DE NUMEROS PEQUEÑOS---"""
"""EN UN EJEMPLO CON UNA ALDEA 1 DE 100 PERSONAS Y ALDEA 2 DE 10000 PERSONAS, QUERIENDO ATRAER HABITANTES
    CONSIGUIERON QUE:
        ALDEA 1 ATRAYERÁ UN 50%
        ALDEA 2 ATRAYERÁ UN 30%
    SIN EMBARGO EL 50% DE 100 ES 50
    Y EL 30% DE 10000 ES 3000
    POR LO QUE AUN CON UN MAYOR PORCENTAJE, EL NUMERO AL COMPARARLO CON UNA POBLACION MUCHO MAS BAJA ES MUCHISIMO MENOR
    TANTO QUE QUE ALDEA2 ATRAJO 60 VECES MAS POBLACION QUE ALDEA 1
"""
aldea1 = 100
aldea2 = 10000

incrementoAldea1 = aldea1 * 0.5
incrementoAldea1

incrementoAldea2 = aldea2 * 0.3
incrementoAldea2

"""porcentajess superiores al 100% totalidad mas valor extra
 si aldea 1 hubiese atraido a 110 personas"""
 (110/aldea1)*100
""" en este caso atrajo a un 110% de su poblacion total"""


""" en este ejercicio calculamos el % de si con respecto al total
"""
array = ["si","si","no","no","si","si"]
p = array.count("si")/len(array)
p * 100
"""66.666%"""
