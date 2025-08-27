# -*- coding: utf-8 -*-
"""
Editor de Spyder
semilla(9)
Este es un archivo temporal.
"""
from numpy.random import seed
from numpy.random import randint
import statistics as st


semillas = 1

seed(semillas) 
"""
el numero de semillas es un patron, no es aleatorio, cualquier persona con
la misma semilla tendra resultados iguales en randint
"""
prueba = randint(0,11, 5)
prueba
"""
randint es: valor minimo, valor maximo, y la cantidad de numeros en el array
"""
edades = randint(5,61, 10)
edades

""" con st.mode usamos statistics para sacar la moda (mode) que significa
    el numero que repite mas entre un listado, en el caso de abajo es el 8"""
edadesModa = [5,10,50,10,13,40,8,8,8]
st.mode(edadesModa)