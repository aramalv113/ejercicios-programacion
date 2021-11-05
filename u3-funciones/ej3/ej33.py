import math
import os
from typing import Type

os.system("cls")

# Cuando se introducen parámetros no numéricos, la función devuelve None
# Cuando no se le pasan valores a la función, esta les asigna 0 a todos los parámetros
def calcula_distancia_puntos(x1=0,x2=0,y1=0,y2=0):
    try:
        return math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))
    except TypeError:
        return None

print(type(calcula_distancia_puntos(1,-1,1,-1)))
