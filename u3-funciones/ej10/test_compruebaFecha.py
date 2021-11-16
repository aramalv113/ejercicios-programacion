from ej10 import compruebaFecha
import pytest

data = [
    (31,1,2021,True), # día 31 de un mes con 31 días
    (31,4,2021,False), # día 31 de un mes con 30 días
    (30,6,2021,True), # día 30 de un mes con 30 días
    (28,2,2021,True), # 28 días de febrero de un año no bisiesto
    (29,2,2021,False), # 29 días de febrero de un año no bisiesto
    (29,2,2020,True), # 29 días de febrero de un año bisiesto
    ('a',2,2021,None), # dato no numerico
    (2,-4,2000,False), # mes negativo
    (-2,4,2000,False), # dia negativo
    (2,4,-2000,False) # año negativo
]

@pytest.mark.parametrize("dia,mes,anio,resultado",data)
def test_eval (dia,mes,anio,resultado):
    assert compruebaFecha(dia,mes,anio) == resultado
