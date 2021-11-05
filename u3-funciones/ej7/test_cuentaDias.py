from ej7 import cuentaDias
import pytest

data = [
    (8,3,2021,67),
    (29,2,2021,-1)
]

@pytest.mark.parametrize("day,month,year,days",data)
def test_eval (day,month,year,days):
    assert cuentaDias(day,month,year) == days