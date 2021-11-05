import os
import math

from _pytest.python_api import approx

os.system("cls")

def calcula_longitud_circunferencia(radio=0):
    try:
        if radio<0:
            return None
        else:
            return 2*math.pi*radio
    except TypeError:
        return None
