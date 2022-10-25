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
    user_answer = input('Хочеш повторити гру? (Y/N): ')
    if user_answer == 'Y':
        game()
    elif user_answer == 'N':
        print('Дякуємо за игру!')
