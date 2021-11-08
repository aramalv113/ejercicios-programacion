from ej7 import *
import pytest

data = [
    (1,1,2020,1,1,2030,10),
    (1,1,2020,1,1,2021,1)
]

@pytest.mark.parametrize("d1,m1,a1,d2,m2,a2,res",data)
def test_eval (d1,m1,a1,d2,m2,a2,res):
    assert calcula_anio_completo(d1,m1,a1,d2,m2,a2) == res