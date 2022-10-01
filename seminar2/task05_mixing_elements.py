# Реализуйте алгоритм перемешивания списка.

import random
random_list = random.sample(range(-10, 10), 10)
def mix_list(random_list):
    random_list = random_list[:]
    list_length = len(random_list)
    for i in range(list_length):
        index_aleatory = random.randint(0, list_length - 1)
        temp = random_list[i]
        random_list[i] = random_list[index_aleatory]
        random_list[index_aleatory] = temp
    return random_list

mixed_list = mix_list(random_list)
print(f'Изначальный список:  {random_list}')
print(f'Перемешанный список:  {mixed_list}')
