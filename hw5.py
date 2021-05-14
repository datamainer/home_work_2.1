import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jockers(user_choise, nouns, adverbs, adjectives):
    repeat = 0

    while repeat != user_choise:
        random_nouns = random.randrange(len(nouns))
        random_adverbs = random.randrange(len(adverbs))
        random_adjectives = random.randrange(len(adjectives))

        print(f'{nouns[random_nouns]} {adverbs[random_adverbs]} {adjectives[random_adjectives]}')

        repeat += 1

user_choise = int(input("введите число колличества рандомных вариантов: "))
get_jockers(user_choise, nouns, adverbs, adjectives)

