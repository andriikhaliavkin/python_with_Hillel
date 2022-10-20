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


convert_to_float(1)
