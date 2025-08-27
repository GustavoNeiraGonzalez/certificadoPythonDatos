# -*- coding: utf-8 -*-
"""
Editor de Spyder
semilla(9)
Este es un archivo temporal.
"""
from numpy.random import seed
from numpy.random import randint

semillas = 1

seed(semillas) 
"""
el numero de semillas es un patron, no es aleatorio, cualquier persona con
la misma semilla tendra resultados iguales en randint
"""
randint(0,11, 5)
"""
randint es: valor minimo, valor maximo, y la cantidad de numeros en el array
"""
seed(semillas) 
edades = randint(5,61, 10)
edades