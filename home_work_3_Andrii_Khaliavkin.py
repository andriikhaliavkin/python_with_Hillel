from essential_generators import DocumentGenerator
import random
import requests

print(
    '''---------------------------------TASK 1----------------------------------------''')
# Зформуйте строку, яка містить певну інформацію про символ по його індексу в відомому слові.
# Наприклад "The [індекс символу] symbol in [тут слово] is '[символ з відповідним порядковим номером]'".
# Слово та номер отримайте за допомогою input() або скористайтеся константою.
# Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in "Python" is 't' ".

# generating a random word from existing:
word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(word_site)
words = response.content.splitlines()
random_word = random.choice(words).decode()
# generating a random symbol's index withing word's length
random_index = random.randint(0, len(random_word) - 1)
# task's solution:
print(f'The {random_index + 1} symbol in word "{random_word}"  is {random_word[random_index]}')

print(
    '''---------------------------------TASK 2----------------------------------------''')
# Вести з консолі строку зі слів за допомогою input() (або скористайтеся константою). Напишіть код, який визначить кількість слів, в цих даних.

# generating a random sentence:
sentence_generator = DocumentGenerator()
random_sentence = sentence_generator.sentence()
# generating a list of words from random sentence:
word_list_from_random_sentence = random_sentence.split()
# task's solution:
print(f'This is a random sentence: \n{random_sentence}')
print(f'This is a list of words from random sentence: \n{word_list_from_random_sentence}')
print(f'Number of words in random sentence: {len(word_list_from_random_sentence)}')

print(
    '''---------------------------------TASK 3----------------------------------------''')
# Існує ліст з різними даними, наприклад lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який сфлрмує новий list (наприклад lst2), який би містив всі числові змінні (int, float), які є в lst1.
# Майте на увазі, що данні в lst1 не є статичними можуть змінюватись від запуску до запуску.


# creating a random number list:
random_number_list = random.sample(range(1, 100), 5)
# creating a random float list:
random_float_list = []
for float in range(0, 5):
    random_float = round(random.uniform(1, 100), 2)
    random_float_list.append(random_float)
# creating a random string list:
random_string_list = sentence_generator.sentence().split()
# creating a random mixed list and shuffling it:
random_mixed_list = random_number_list + random_float_list + random_string_list
random.shuffle(random_mixed_list)


# creating a function to sort data by its type
def typed_lists(random_list):
    string_list = []
    int_list = []
    float_list = []

    for item in random_list:
        if type(item) == int:
            int_list.append(item)
        elif type(item) == str:
            string_list.append(item)
        else:
            float_list.append(item)
    print(f'List with integers: \n{int_list}')
    print(f'List with strings: \n{string_list}')
    print(f'List with floats: \n{float_list}')


# task's solution:
print(f'Mixed list: \n{random_mixed_list}')
typed_lists(random_mixed_list)
