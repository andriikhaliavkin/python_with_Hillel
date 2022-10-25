# Напишіть гру "Вгадай число":
# програма загадує число від 1 до 100 і користувач намагається його вгадати.
# якщо вгадав - вивести повідомлення "Поздоровляємо!"
# якщо невгадав і різниця між числом користувача і загаданим більше 10 - вивести повідомлення "Холодно", якщо 5-10 - "Тепло", якщо 1-4 "Гаряче".
# після того, як користувач вгадав число - запитати, чи хоче він повторити гру (Y\N)
# всі функцій, крім основної, помістіть в окремий файл і імпортуйте в основний файл.
# Напишіть декоратор, який вимірює і виводить на екран час виконання функції в секундах і задекоруйте ним основну функцію гри.
# Після закінчення гри декоратор має сповістити, скільки тривала гра.

import random
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f'Game duration: {end - start} seconds')

    return wrapper


def main():
    while True:
        print('Guess the number from 1 to 100')
        number = random.randint(1, 100)
        guess = 0
        while guess != number:
            guess = int(input('Your guess: '))
            if guess > number:
                print('Too high')
            elif guess < number:
                print('Too low')
            else:
                print('Congratulations!')
        answer = input('Do you want to play again? (Y/N) ')
        if answer.lower() == 'n':
            break

main()
timer(main)
