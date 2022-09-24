# Реализуйте алгоритм перемешивания списка.
import random
random_list = random.sample(range(-10, 10), 10)
def shuffle(random_list):
    random_list = list(random_list)
    random.shuffle(random_list)
    return random_list


mixing_list = shuffle(random_list)
print(f'Первоначальный список: {random_list}')
print(f'Перемешанный список: {mixing_list}')