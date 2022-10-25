# Напишіть гру "Вгадай число":
# програма загадує число від 1 до 100 і користувач намагається його вгадати.
# якщо вгадав - вивести повідомлення "Поздоровляємо!"
# якщо невгадав і різниця між числом користувача і загаданим більше 10 - вивести повідомлення "Холодно", якщо 5-10 - "Тепло", якщо 1-4 "Гаряче".
# після того, як користувач вгадав число - запитати, чи хоче він повторити гру (Y\N)
# Напишіть декоратор, який вимірює і виводить на екран час виконання функції в секундах і задекоруйте ним основну функцію гри.
# Після закінчення гри декоратор має сповістити, скільки тривала гра.

import random
import time

def decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print('час гри: ', end_time - start_time)
    return wrapper

@decorator
def game():
    number = random.randint(1, 100)
    while True:
        user_number = int(input('Введіть число: '))
        if user_number == number:
            print('Поздоровляємо!')
            break
        elif abs(user_number - number) > 10:
            print('Холодно')
        elif 5 <= abs(user_number - number) <= 10:
            print('Тепло')
        elif 1 <= abs(user_number - number) <= 4:
            print('Гаряче')
    user_answer = input('Хочешь повторити гру? (Y/N): ')
    if user_answer == 'Y':
        game()
    elif user_answer == 'N':
        print('Дякуємо за игру!')

game()



