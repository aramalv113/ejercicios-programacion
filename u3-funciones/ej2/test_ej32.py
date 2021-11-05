from ej32 import *
import pytest

def test_radio_positivo():
    assert calcula_longitud_circunferencia(5) == pytest.approx(31.4,0.1),"Fallo test radio positivo"
def test_radio_cero():
    assert calcula_longitud_circunferencia(0) == 0,"Fallo test radio cero"

def test_radio_negativo():
    assert calcula_longitud_circunferencia(-3) is None,"Fallo test radio negativo"

def test_radio_no_numerico():
    assert calcula_longitud_circunferencia('a') is None,"Fallo test radio no numerico"

def test_radio_float():
    assert calcula_longitud_circunferencia(2.32) == pytest.approx(14.57,0.001),"Fallo test radio float"

def test_radio_sin_valor():
    assert calcula_longitud_circunferencia() == 0,"Fallo radio sin valor"



