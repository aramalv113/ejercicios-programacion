from _pytest.compat import assert_never
from ej9 import adivina_numero
import pytest

data = [
    (30,20,2),
    (10,20,3),
    (18,20,1),
    (20,20,0),
    ('a',20,None),
    (18,'a',None)
]

@pytest.mark.parametrize("num1,num2,res",data)
def test_eval (num1,num2,res):
    assert adivina_numero(num1,num2) == res