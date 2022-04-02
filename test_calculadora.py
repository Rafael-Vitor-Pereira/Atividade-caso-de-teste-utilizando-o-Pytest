from calculadora import Calculadora
import pytest
calc = Calculadora()

def test_soma():
  assert calc.Soma(12, 5) == 17

def test_subtrai():
  assert calc.Subtrracao(12, 5) == 7

def test_multiplica():
  assert calc.Multiplicacao(12, 5) == 60

def test_divisao():
  with pytest.raizes(valueError):
    calc.Divisao(12, 5)