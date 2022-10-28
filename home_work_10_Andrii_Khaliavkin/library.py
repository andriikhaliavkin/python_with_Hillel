# потрібно дописати is_string_capitalized (в тому числі докстрінги) - очікування - прохід тестів

def is_string_capitalized(string):
    """
    This function checks if the first letter of the string is capitalized.
    :param string: string
    :return: bool
    """
    if string == '':
        return True
    elif string.isalnum():
        return True
    elif string[0].isupper() and string[1:].islower() == True:
        return True
    elif string[0].isupper() and string[1:].islower() == False:
        return False
    else:
        return False


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
