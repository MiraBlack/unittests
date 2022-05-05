def calculator(expression):

    allowed_symbols = '+-/*'

    if not any (symbol in expression for symbol in allowed_symbols):
        raise ValueError(f'Выражение должно содержать знак из списка ({allowed_symbols})')
    for symbol in allowed_symbols:
        if symbol in expression:
            try:
                first_number, second_number = map(lambda x: int(x), (expression.split(symbol)))
                return {
                    '+': lambda x, y : x+y,
                    '-': lambda x, y : x-y,
                    '/': lambda x, y : x/y,
                    '*': lambda x, y : x*y
                } [symbol] (first_number, second_number)
            except (ValueError, TypeError):
                raise ValueError('Выражение должно содержать 2 целых числа и 1 знак')

