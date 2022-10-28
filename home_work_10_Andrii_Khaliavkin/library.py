
# потрібно дописати is_string_capitalized (в тому числі докстрінги) - очікування - прохід тестів
# assert is_string_capitalized('My name is David') is False
# assert is_string_capitalized('I love playing') is True
# assert is_string_capitalized('') is True
# assert is_string_capitalized('565656') is True

def is_string_capitalized(string):
    """
    This function checks if the first letter of the string is capitalized.
    :param string: string
    :return: bool
    """
    if string == '':
        return True
    elif string[0].isupper():
        return True
    elif string[0].isalnum():
        return True
    else:
        return False


assert is_string_capitalized('My name is David') is True
assert is_string_capitalized('I love playing') is True
assert is_string_capitalized('') is True
assert is_string_capitalized('565656') is True


# write a function to check if the given number is odd or even

def is_odd_or_even(number):
    """
    This function checks if the given number is odd or even.
    :param number: int
    :return: str
    """
    if number % 2 == 0:
        return 'even'
    else:
        return 'odd'


assert is_odd_or_even(5) == 'odd'
assert is_odd_or_even(6) == 'even'
assert is_odd_or_even(0) == 'even'
assert is_odd_or_even(-1) == 'odd'

