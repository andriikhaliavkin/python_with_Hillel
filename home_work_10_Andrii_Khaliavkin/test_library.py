import library

assert library.is_string_capitalized('My name is David') is False
assert library.is_string_capitalized('I love playing') is True
assert library.is_string_capitalized('') is True
assert library.is_string_capitalized('565656') is True