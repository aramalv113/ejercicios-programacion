from ej10 import calcula_anio_completo
import pytest

data = [
    (1,1,2020,1,1,2030,10), # fecha correcta en distintos años
    (1,1,2020,2,2,2020,0), # fecha correcta en mismo año
    (29,2,2021,1,1,2025,-1), # fecha 1 incorrecta
    (22,2,2021,29,2,2025,-1), # fecha 2 incorrecta
    ('a',1,2020,'b',2,2020,None) # parámetros ilegales
]

@pytest.mark.parametrize("d1,m1,a1,d2,m2,a2,res",data)
def test_eval (d1,m1,a1,d2,m2,a2,res):
    assert calcula_anio_completo(d1,m1,a1,d2,m2,a2) == res