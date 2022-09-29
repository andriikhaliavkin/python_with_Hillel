from essential_generators import DocumentGenerator
import random
import requests

# Зформуйте строку, яка містить певну інформацію про символ по його індексу в відомому слові.
# Наприклад "The [індекс символу] symbol in [тут слово] is '[символ з відповідним порядковим номером]'".
# Слово та номер отримайте за допомогою input() або скористайтеся константою.
# Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in "Python" is 't' ".

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(word_site)
words = response.content.splitlines()
random_word = random.choice(words)
print(random_word)


print(
    '''-------------------------------------------------------------------------------''')
# Вести з консолі строку зі слів за допомогою input() (або скористайтеся константою). Напишіть код, який визначить кількість слів, в цих даних.

sentence_generator = DocumentGenerator()
random_sentence = sentence_generator.sentence()
word_list_from_random_sentence = random_sentence.split()
print(random_sentence)
print(word_list_from_random_sentence)
print(f'Кількість слів у припадковому реченні: {len(word_list_from_random_sentence)}')


# Існує ліст з різними даними, наприклад lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який сфлрмує новий list (наприклад lst2), який би містив всі числові змінні (int, float), які є в lst1.
# Майте на увазі, що данні в lst1 не є статичними можуть змінюватись від запуску до запуску.

print(
    '''-------------------------------------------------------------------------------''')
#Creating a random list with mixed data types (int / float / string) and shuffle it.
random_number_list = random.sample(range(1, 100), 5)
random_float_list = []
for float in range(0, 5):
    random_float = round(random.uniform(1, 100), 2)
    random_float_list.append(random_float)
random_string_list = sentence_generator.sentence().split()
random_mixed_list = random_number_list + random_float_list + random_string_list
random.shuffle(random_mixed_list)
print(random_mixed_list)

#creating a function to sort data by it's type


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
    print(int_list)
    print(string_list)
    print(float_list)

typed_lists(random_mixed_list)
