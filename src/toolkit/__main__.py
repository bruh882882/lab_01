import sys

from toolkit.calculator import calc
from toolkit.converter import convert
from toolkit.errors import CalculatorError, ConverterError


def main():
    arguments = sys.argv[1:]
    
    if '--help' in arguments:
        print('Набор консольных утилит')
        print("- _ -'")
        print("Использование:")
        print("  python -m toolkit calc expression")
        print("  python -m toolkit convert float_value unit_1 unit_2")
        print("  python -m toolkit --help")
        sys.exit(0)
    
    command = arguments[0]
    
    if command == 'convert':
        if len(arguments) != 4:
            print('Неверное количество аргументов')
            sys.exit(2)
        valuee = arguments[1]
        unit_1 = arguments[2]
        unit_2 = arguments[3]

        try:
            value = float(valuee)
        except ValueError:
            print("Ошибка ввода значения", file = sys.stderr)
            sys.exit(2)

        try:
            result = convert(value, unit_1, unit_2)
            print(result)
            sys.exit(0)
        except ConverterError as err:
            print(f"{err}", file = sys.stderr)
            sys.exit(2)

    elif command == 'calc':
        if len(arguments) != 2:
            print("Передайте выражение в ковычках например: calc ""2 + 2 * 2"", скокбки не поддерживаются")
            sys.exit(2)

        expression = arguments[1]

        try:
            result = calc(expression)
            print(result)
            sys.exit(0)
        except CalculatorError as err:
            print(f"{err}", file = sys.stderr)
            sys.exit(2)

    else:
        print("Неизвестная команда", file = sys.stderr)
        sys.exit(2)

if __name__ == "__main__":
    main()