import library

assert library.is_string_capitalized('My name is David') is False
assert library.is_string_capitalized('I love playing') is True
assert library.is_string_capitalized('') is True
assert library.is_string_capitalized('565656') is True

assert library.is_odd_or_even(5) == 'odd'
assert library.is_odd_or_even(6) == 'even'
assert library.is_odd_or_even(0) == 'even'
assert library.is_odd_or_even(-1) == 'odd'




