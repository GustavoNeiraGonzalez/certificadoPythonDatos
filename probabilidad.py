# -*- coding: utf-8 -*-
"""
Created on Fri Aug 29 16:53:04 2025

@author: tavo-
"""

""" probabilidad teorica 

Lanzamientos de monedas. Frente a la pregunta sobre la probabilidad
de obtener cara en un lanzamiento, Ia respuesta o
probabilidad teórica es 1/2, esto es, la frecuencia del
evento o "éxito" cara), repartido o dividido entre el
total de estados posibles (2= cara o sello).

Lo mismo aplica para los dados y la
probabilidad de obtener cualquier
número en un lanzamiento (1/6).
"""


""" probabilidad empirica
en muchos casos de la vida no se puede sacar una probabilidad a simple vista,
para poder sacar la probabilidad empirica se necesitan datos

personas que tienen 60 años o más, y dividirla entre el
total de la población.
Una parte importante del trabajo estadístico es
justamente, de manera inductiva, es decir, desde los
datos, la probabilidad teórica esperada. No obstante,
en el mundo real existe Ia incertidumbre y Ia
aleatoriedad, por lo que el recogimiento de datos no es
perfecto, o fluctúa, pudiendo dar valores distintos a los
esperados por la probabilidad teórica.
"""

from numpy.random import seed
from numpy.random import randint
from numpy import mean

seed(1234)
lanzamientos = randint(0,2,100000)

sum(lanzamientos)/100000
"""
    el resultado es 0.525% donde al partir de 0. 0 seria cruz y 1 cara, sumando todo te da resultado de las veces 
    que salio cara 

    si bien el resultado esperado no es 0.5, no es muy diferente a la probabilidad esperarada
    ----LEY DE LOS GRANDES NUMEROS---
    tambien por puro azar puede ser que en numeros mas bajos este resultado pueda que solo toquen caras, o el 90%
    pero mientras mas cantidad de repeticiones le damos MAS improbable es que el resultado final se distancie del esperado
    de 10 intentos 10 pueden ser caras de 100 imagina que 100 fueron caras, pero de 1000? 10000? o mas? el azar perderia
    casi por completo esa capacidad"""

""" en este ejemplo sacamos la probabilidad sacada del numero 6 en 100 tiros de dados"""
sum(randint(1, 7, 100)==6)/100

"""con el bucle for simulamos 10 lanzamientos de moneda un millon de veces y los guarda en eventos,
    dicho esto podemos buscar las primeras 10 veces que se simulo los 10 lanzamientos para ver que resultados
    hubó
    (se tardará un momento por la enorme cantidad en el bucle)"""
eventos = []
for i in range(1, 1000000):
    eventos.append(sum(randint(0, 2, 10))/10)
eventos[1:10]
"""
los resultados de los primeros 10 intentos son:
    0.5, 0.6,0.2,0.4,0.2,0.4,0.8,0.7,0.6
"""

mean(eventos)

""" el resultado es 0.50008... con numeros mucho mas grandes el resultado se iguala"""
