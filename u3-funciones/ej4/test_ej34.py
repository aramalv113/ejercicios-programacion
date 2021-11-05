from ej34 import *
import pytest

data = [
    ('a',1,None),
    (1,1,2),
    (-1,1,0),
    (5,-5,1),
    (5,1.2,6),
    (1.8,4,pytest.approx(22.36,0.01)),
    (2,0,1),
    (0,2,1)
]

@pytest.mark.parametrize("data1,data2,result",data)
def test_eval (data1, data2, result):
    assert calcula_progresion_geometrica(data1,data2) == result,"Fallo"