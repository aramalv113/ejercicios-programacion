from ej10 import convierte_en_dias
import pytest

data = [
    (8,3,2021,67), # fecha correcta
    (29,2,2021,-1), # fecha incorrecta
    ('a',4,'b',None) # parámetros ilegales
]

@pytest.mark.parametrize("day,month,year,days",data)
def test_eval (day,month,year,days):
    assert convierte_en_dias(day,month,year) == days