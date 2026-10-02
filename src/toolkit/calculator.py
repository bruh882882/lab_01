from toolkit.errors import CalculatorError

symbols = '+-*/'
digits = '0123456789'

def tokenization(raw_expression: str):
    expression = raw_expression.replace(" ", "")
    
    if not expression:
        raise CalculatorError("Пустое выражение")

    tokens = []
    i = 0
    length = len(expression)
    while i < length:
        ch = expression[i]

        if ch in digits or ch == '.':
            num_str = ""
            dot = 0
            while i < length and (expression[i] in digits or expression[i] == '.'):
                if expression[i] == '.':
                    dot += 1
                num_str += expression[i]
                i += 1

            if dot > 1: 
                raise CalculatorError("Неверное числовое значение")
            if '.' in num_str:
                tokens.append(float(num_str))
            else:
                tokens.append(int(num_str))

            continue

        elif ch in symbols:
            tokens.append(ch)
            i += 1

        else: 
            raise CalculatorError("Некорректный ввод")
    return tokens

def validation(tokens):

    if str(tokens[0]) in symbols[2:4] or str(tokens[-1]) in symbols:
        raise CalculatorError("Пропущено число")

    valid_tokens = []
    i = 0
    n = len(tokens)

    while i < n:
        token = tokens[i]

        if (str(token) in symbols[0:2]) and ((i == 0) + (str(tokens[i-1]) in symbols) > 0): 
            if (i + 1 >= n) or (str(tokens[i+1]) in symbols):
                raise CalculatorError("Пропущен опреднд")

            potentially_negative_num = tokens[i+1]
            if token == '-':
                num = -potentially_negative_num
            else:
                num = potentially_negative_num
            valid_tokens.append(num)
            i += 2
            continue

        if str(token) in symbols and i > 0 and str(tokens[i-1]) in symbols:
            raise CalculatorError('Два бинарных оператора подряд')

        valid_tokens.append(token)
        i += 1

    return valid_tokens

def calculation(tokens):

    i = 0
    while i < len(tokens):
        if str(tokens[i]) in symbols[2:4]:
            oper1 = tokens[i]
            left1 = tokens[i-1]
            right1 = tokens[i+1]

            if oper1 == '*':
                result1 = left1 * right1
            else: 
                if right1 == 0:
                    raise CalculatorError('Деление на ноль')
                result1 = left1 / right1

            tokens[i-1:i+2] = [result1]
            continue
        i += 1

    i = 0 
    while i < len(tokens):
        if str(tokens[i]) == '+' or str(tokens[i]) == '-':
            oper2 = tokens[i]
            left2 = tokens[i-1]
            right2 = tokens[i+1]

            if oper2 == '+':
                result2 = left2 + right2 
            else:
                result2 = left2 -  right2 

            tokens[i-1:i+2] = [result2]
            continue
        i += 1

    if len(tokens) == 1:
        return float(tokens[0])

def calc(expression: str):

    tokens = tokenization(expression)
    valid_tokens = validation(tokens)
    calculated_tokens_result = calculation(valid_tokens)

    return round(calculated_tokens_result, 10)