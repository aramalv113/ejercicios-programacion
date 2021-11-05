from ej33 import *
import pytest

def test_prueba():
    assert calcula_distancia_puntos(1,1,1,1) == 0,"Fallo test prueba"

def test_valores_negativos():
    assert calcula_distancia_puntos(1.4,-1.5,-2.3,-1.7) == pytest.approx(2.96,0.01),"Fallo resultado esperado"

def test_valores_no_numericos():
    assert calcula_distancia_puntos(0,1,"hola",2) is None,"Fallo datos no numericos"

def test_no_introduce_valores():
    assert calcula_distancia_puntos() == 0,"Fallo no introduce valores"

def test_valor_infinito():
    assert calcula_distancia_puntos(math.inf,1,3,2) == math.inf,"Fallo valor infinito"