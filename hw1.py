def num_translate(user_numbers):
    "переводчик чисел с английского на русский"

    numbers = {'one':'один',
             'two': 'два', 
             'three':'три', 
             'four': 'четыре', 
             'five':'пять', 
             'six':'шесть', 
             'seven':'семь', 
             'eight':'восемь',
             'nine':'девять',
             'ten':'десять',
             'One':'Один',
             'Two': 'Два', 
             'Three':'Три', 
             'Four': 'Четыре', 
             'Five':'Пять', 
             'Six':'Шесть', 
             'Seven':'Семь', 
             'Eight':'Восемь',
             'Nine':'Девять',
             'Ten':'Десять'}

    print(numbers.get(user_numbers, 'такого числа нет'))


user_numbers = input('введите число буквами от 1 до 10: ')
num_translate(user_numbers)