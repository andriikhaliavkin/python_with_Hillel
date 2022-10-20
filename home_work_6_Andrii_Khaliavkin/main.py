print(
    '''---------------------------------TASK 1----------------------------------------''')


# Напишіть функцію, що приймає один аргумент будь-якого типу та повертає цей аргумент,
# перетворений на float. Якщо перетворити не вдається функція має повернути 0.

def convert_to_float(arg):
    """Take number as arg, return float or 0"""
    try:
        return float(arg)
    except ValueError:
        return 0


print(convert_to_float('123'))

print(
    '''---------------------------------TASK 2----------------------------------------''')


# Напишіть функцію, що приймає два аргументи. Функція повинна
# якщо аргументи відносяться до числових типів (int, float) - повернути перемножене значення цих аргументів,
# якщо обидва аргументи це строки (str) - обʼєднати в одну строку та повернути
# у будь-якому іншому випадку повернути кортеж з цих аргументів

def multiply_or_concat(arg1, arg2):
    """Take two args, return multiplication or concatenation"""
    if isinstance(arg1, (int, float)) and isinstance(arg2, (int, float)):
        return arg1 * arg2
    elif isinstance(arg1, str) and isinstance(arg2, str):
        return arg1 + arg2
    else:
        return arg1, arg2


print(multiply_or_concat('d', 'f'))
