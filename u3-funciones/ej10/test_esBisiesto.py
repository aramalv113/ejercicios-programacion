from ej10 import esBisiesto
import pytest

values = [
    (1986, False),
    ('a', None),
    (-1986, None),
    (1986.89, False)
]

@pytest.mark.parametrize("data,result",values)
def test_eval(data,result):
    assert esBisiesto(data) == result,"Fallo"
