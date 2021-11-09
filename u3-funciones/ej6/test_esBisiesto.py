from ej6 import esBisiesto
import pytest

data = [
    (1986, False),
    ('a', None),
    (-1986, None),
    (1986.89, False)
]

@pytest.mark.parametrize("year,result",data)
def test_eval (year,result):
    assert esBisiesto(year) == result