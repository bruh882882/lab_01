Лабораторная работа 1. Консольный набор утилит

Выполнил: Ларионов Матвей Дмитриевич, группа М8О-103БВ-26

Структура работы:
lab_01/
    pyproject.toml
    README.md
    src/toolkit/
        __init__.py
        __main__.py
        calculator.py
        converter.py
        errors.py
    tests/
        __init__.py
        test_toolkit.py

Поддерживаемые команды:
python -m toolkit calc "expression" (скобки не поддерживаются)
python -m toolkit convert float_value unit_1 unit_2
python -m toolkit --help

Код соответсвует стандарту PEP8 (проверен ruff check .)
