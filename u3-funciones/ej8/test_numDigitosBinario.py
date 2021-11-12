from ej8 import num_digitos_binarios
import pytest

data = [
    (0,1), # número de 1 bit
    (125,7), # número de 7 bits
    ('a',None), # parámetro ilegal
    (-5,0) # número negativo
]

@pytest.mark.parametrize("decimal,digitos",data)
def test_eval (decimal, digitos):
    assert num_digitos_binarios(decimal) == digitos