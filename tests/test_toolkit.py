import sys

import pytest

from toolkit.__main__ import main
from toolkit.calculator import calc
from toolkit.converter import convert
from toolkit.errors import CalculatorError, ConverterError


def test_calc_basic(): #Тест 1: Базовое сложение, вычитание, умножение и деление
    assert calc("2 + 2") == 4.0
    assert calc("10 - 4") == 6.0
    assert calc("3 * 4") == 12.0
    assert calc("10 / 2") == 5.0

def test_calc_operations_priority(): #Тест 2: Приоритет операторов 
    assert calc("2 + 3 * 4") == 14.0
    assert calc("10 - 4 / 2") == 8.0

def test_calc_unary_operators(): #Тест 3: Унарные плюсы и минусы
    assert calc("-5 + 3") == -2.0
    assert calc("5 * -2") == -10.0
    assert calc("+5 + +3") == 8.0

def test_calc_floats_and_spaces(): #Тест 4: Работа с пробелами и числами с плавающей точкой
    assert calc("  2.5   *   2  ") == 5.0
    assert calc("0.1 + 0.2") == 0.3

def test_calc_error_division_by_zero(): #Тест 5: Ошибка деления на ноль
    with pytest.raises(CalculatorError):
        calc("10 / 0")

def test_calc_error_invalid_tokens(): #Тест 6: Ошибка при вводе запрещенных символов
    with pytest.raises(CalculatorError):
        calc("2 + 2x")
    with pytest.raises(CalculatorError):
        calc("5.5.5 + 1")

def test_calc_error_missing_operands(): #Тест 7: Ошибка отсутствия чисел рядом со знаками
    with pytest.raises(CalculatorError):
        calc("5 *")
    with pytest.raises(CalculatorError):
        calc("+ * 3")

def test_convert_length(): #Тест 8: Перевод единиц длины
    assert convert(1, "km", "m") == 1000.0
    assert convert(10, "mm", "cm") == 1.0

def test_convert_mass(): #Тест 9: Перевод единиц массы
    assert convert(5, "kg", "g") == 5000.0
    assert convert(500, "g", "kg") == 0.5

def test_convert_temperature(): #Тест 10: Перевод температур
    assert convert(0, "c", "k") == 273.15
    assert convert(32, "f", "c") == 0.0

def test_convert_error_different_groups(): #Тест 11: Ошибка при попытке перевести длину в массу
    with pytest.raises(ConverterError):
        convert(10, "m", "kg")

def test_convert_error_absolute_zero(): #Тест 12: Ошибка при температуре ниже абсолютного нуля
    with pytest.raises(ConverterError):
        convert(-300, "c", "k")

def test_cli_calc_success(monkeypatch, capsys): #Тест 14: Проверка успешного выполнения команды calc
    monkeypatch.setattr(sys, "argv", ["__main__.py", "calc", "10 + 5"])
    
    with pytest.raises(SystemExit) as sample:
        main()
        
    assert sample.value.code == 0
    captured = capsys.readouterr()
    assert "15.0" in captured.out  

def test_cli_error_unknown_command(monkeypatch, capsys): #Тест 15: CLI падает с кодом 2 при неизвестной команде

    monkeypatch.setattr(sys, "argv", ["__main__.py", "бебебе"])
    
    with pytest.raises(SystemExit) as sample:
        main()
        
    assert sample.value.code == 2 
    captured = capsys.readouterr()
    assert "Неизвестная команда" in captured.err