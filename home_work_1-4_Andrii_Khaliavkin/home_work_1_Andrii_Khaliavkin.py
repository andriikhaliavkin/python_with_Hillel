# Задача: Створіть дві змінні first=10, second=30. Виведіть на екран результат математичної взаємодії (+, -, *, / и тд.) для цих чисел.

first = 10
second = 30

print(first + second)
print(first - second)
print(first * second)
print(first / second)
print(first // second)
print(first % second)
print(first ** second)

# Задача: Створіть змінну і запишіть в неї результат порівняння (<, > , ==, !=) чисел з завдання 1. Виведіть на екран результат кожного порівняння.

comparison = first > second
print(comparison)

comparison = first < second
print(comparison)

comparison = first == second
print(comparison)

comparison = first != second
print(comparison)

# Задача: Створіть змінну - результат конкатенації (складання) строк str1="Hello " и str2="world". Виведіть на екран.

str1 = "Hello "
str2 = "world"

str3 = str1 + str2
print(str3)
print(str1 + str2)
print(f'{str1}{str2}')