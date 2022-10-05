import numpy as np
test_dict = {'a': 1.1, 'b': 2.234, 'c': 3.098, 'd': 4.333, 'e': 5.098, 'f': 6.999, 'g': 7.343, 'h': 8.23434,
             'i': 9.030, 'j': 10.234}
val_list = list(test_dict.values())
key_list = list(test_dict.keys())

#if i in val_list in range(1.00, 5.00) print key_list[i]
for i in range(len(val_list)):
    if 1.00 <= val_list[i] <= 5.1:
        print(key_list[i])


