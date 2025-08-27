# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 16:46:41 2025

@author: tavo-
"""
"""----MODA---"""
""" con st.mode usamos statistics para sacar la moda (mode) que significa
    el VALOR que repite mas entre un listado, en el caso de abajo es el 8
   tambien puede ser el texto que mas se repita"""
from numpy.random import seed
from numpy.random import randint
import statistics as st


semillas = 132
seed(semillas) 


edadesModa = [5,4,50,10,13,40,8,8,8]
moda = st.mode(edadesModa)
moda

edadesModa2 = [5,4,50,10,13,40,8]
modaSinRepetidos = st.mode(edadesModa2)
modaSinRepetidos

listadoTexto = ["ministro","presidente","ministro","dictador"]
modaTexto = st.mode(listadoTexto)
modaTexto

"""----MEDIANA---"""
from numpy import quantile
""" con mediana buscamos el valor a la mitad es decir que sea el 50% inferior y el 50% superior
usando quantile(x, 0.5)
Esto implica que si dividimos la variable
en dos, una mitad es inferior a 4 (1 al 3), y
la segunda es mayor (5 al 7). es decir 3 numeros por debajo y 3 por encima"""
numeros = list(range(1,8))

mediana = quantile(numeros,0.5)
mediana

numerosDesordenados = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]
medianaDesordenada = quantile(numerosDesordenados,0.5)
medianaDesordenada
"""La respuesta es 5.5 ¿por qué? Aquí ocurren 2
cosas. Primero, los elementos son ordenados
del menor al mayor, y luego se busca el valor
del centro que permita dividir los datos en dos
mitades. No obstante, en este caso no hay un
valor en el medio, ya que la cantidad de
números es par, por lo tanto, la función toma
los 2 valores del medio, y los divide por dos,
para encontrar el centro del centro."""

"""--no mediana pero usando el 25% inferior, y el 90%--"""

"""Esto implica que el 25% de los datos (del 2 al 3) es menor que 3.5, y el 75% restante (del 4 al 12) es mayor.
Notar que esta vez tuvimos que especificar el parámetro "interpolation" y fijarlo a midpoint. Esto se debe a que existen
varias formas de calcular cuantiles, y en este caso estamos usando el punto medio."""
numeros = [11, 2, 4, 6, 8, 10, 1, 3, 7, 9, 11, 12]

cuarto = quantile(numeros, 0.25, interpolation= 'midpoint')
cuarto
"""3.5 es el 25%"""
noventa = quantile(numeros, 0.90, interpolation= 'midpoint')
noventa
""" aqui el 90% es 11"""

"""Puedes cambiar el valor por lower, higher, nearest o linear, 
todos los cuales dan distintos resultados que van de 3 a 4;
todas son respuestas correctas, pero para nuestros efectos, usar el punto medio nos resulta más interpretable.
Juega un poco con los cuantiles, y trata de obtener el cuantil 75%, el 90% o el 1% de un conjunto de datos."""


"""------PROMEDIO-----"""
""""Hay 2 computadoras.
Tú tienes dos. Yo ninguna.
Computadoras promedio:
una por persona

Similar a los estadísticos anteriores, el promedio también es una medida que intenta capturar el centro de los datos,
pero distinto de la mediana y la moda, considera la totalidad de los datos disponibles, sumándolos, y dividiéndolos
por Ia cantidad de datos disponibles, de esta forma:
    4+5+10+5 = 24
    24/4 = 6 PROMEDIO 6"""
from numpy import mean
numeros = [15, 16, 16, 17, 17, 18, 19, 19, 20, 21]
promedio = mean(numeros)
promedio
"""promedio igual 17.8 (total/cantidad)"""


"""desviacion estandar
Para obtener la desviación estándar realizamos los siguientes pasos. A cada valor le restamos el promedio, este valor
lo elevamos al cuadrado para compensar posibles valores negativos, y luego le sacamos Ia raíz cuadrada para
devolverlos a su unidad de medida original

Por ejemplo, en el caso del computador, si bien
teníamos un promedio de 1 computador por
persona, al ser la desviación estándar de 1, implica
que hay personas que podían tener 2 computadores
(promedio + desviación estándar —> 1 + 1), así como
hay personas que podrían tener O (promedio -
desviación estándar —> 1 - 1).
Es por ello que siempre que se vea o reporte un
promedio, es necesario tener presente la medida de
desviación o en última instancia, la mediana, a fin de
tener una idea de cómo están distribuidos los datos,
y entender mejor el promedio."""
from numpy import std
computador_por_persona = [2, 0]
promedioDesviacionEstandar = std(computador_por_persona)
promedioDesviacionEstandar







