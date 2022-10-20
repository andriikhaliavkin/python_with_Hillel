# Є дікт, невідомого наповнення. В дікті присутні ключі, занченням для яких є дікти невідомого наповнення в яких можуть бути аналогічні вкладені дікти.
# Напишіть функцію, яка дістане всі ключі зі значеннями не-діктами з усіх рівнів вкладення, помістить на один рівень в окремий дікт і поверне цей дікт.
# Напишіть докстрінг для цієї функці.

def get_all_keys(d):
    """
    The function returns a dictionary with all keys from the dictionary with nested dictionaries.
    """
    result = {}
    for key, value in d.items():
        if type(value) == dict:
            result.update(get_all_keys(value))
        else:
            result[key] = value
    return result

print(get_all_keys({'a': 1, 'b': {'c': 2, 'd': {'e': 3, 'f': 4}}}))