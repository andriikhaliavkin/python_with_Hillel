from essential_generators import DocumentGenerator

print(
    '''---------------------------------TASK 1----------------------------------------''')
# Дана довільна строка. Напишіть код, який знайде в ній і віведе на екран кількість слів, які містять дві голосні літери підряд.

vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
# generating a random sentence:
sentence_generator = DocumentGenerator()
random_sentence = sentence_generator.sentence()
# generating a list of words from random sentence:
word_list_from_random_sentence = random_sentence.split()

print(word_list_from_random_sentence)

words_with_pair_vowels = set()

for word in word_list_from_random_sentence:

    list_of_letters_in_the_word = []
    list_of_letters_in_the_word.extend(word)

    for letter in range(len(list_of_letters_in_the_word) - 1):
        if list_of_letters_in_the_word[letter] in vowels and list_of_letters_in_the_word[letter + 1] in vowels:
            words_with_pair_vowels.add(word)

if len(words_with_pair_vowels) == 0:
    print('There is no any word with pair vowels')
elif len(words_with_pair_vowels) == 1:
    print(f'There is only 1 word with pair vowels: {words_with_pair_vowels}')
else:
    print(f'The are {len(words_with_pair_vowels)} words with pair vowels: {words_with_pair_vowels}')

print(
    '''---------------------------------TASK 2----------------------------------------''')
# Є два довільних числа які відповідають за мінімальну і максимальну ціну. Є Dict з назвами магазинів і цінами:
# { "cito": 47.999, "BB_studio" 42.999, "momo": 49.999, "main-service": 37.245, "buy.now": 38.324, "x-store": 37.166,
# "the_partner": 38.988, "store": 37.720, "rozetka": 38.003}. Напишіть код, який знайде і виведе на екран назви магазинів,
# ціни яких попадають в діапазон між мінімальною і максимальною ціною.

stores_with_prices = {"cito": 47.999, "BB_studio": 42.999, "momo": 49.999, "main-service": 37.245, "buy.now": 38.324,
                      "x-store": 37.166, "the_partner": 38.988, "store": 37.720, "rozetka": 38.003}

while True:
    try:
        min_price = float(input('provide minimum price: '))
        max_price = float(input('provide maximum price: '))
        if min_price < 0 or max_price < 0 or max_price < min_price:
            print('Please enter correct price range (without negative values, max price should be higher then min '
                  'price.)')
            continue
        break
    except ValueError as e:
        print('Please enter prices in numbers: ')

print(min_price)
print(max_price)

