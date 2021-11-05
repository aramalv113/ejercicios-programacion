from ej31 import *
import pytest
import math

def test_resultado_correcto():
    assert calcula_area_triangulo(1,1) == 0.5,"Fallo resultado correcto"

def test_valores_no_numericos():
    assert calcula_area_triangulo('a',3) is None, "Fallo valores no numericos"

def test_base_negativa():
    assert calcula_area_triangulo(-3,5) is None,"Fallo base negativa"

def test_altura_negativa():
    assert calcula_area_triangulo(5,-3) is None,"Fallo altura negativa"

def test_valores_negativos():
    assert calcula_area_triangulo(-1,-4) is  None,"Fallo valores negativos"

def test_base_infinita():
    assert calcula_area_triangulo(math.inf,4) == math.inf,"Fallo base infinita"
    
def test_altura_infinita():
    assert calcula_area_triangulo(4,math.inf) == math.inf,"Fallo altura infinita"

def test_indeterminacion():
    assert calcula_area_triangulo(0,math.inf) is math.nan,"Fallo indeterminacion"