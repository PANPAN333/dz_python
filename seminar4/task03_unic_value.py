# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


from random import randrange


def unic_value(random_list): # функция отсеивания и сортировки random_list
    return [i for i in set(random_list)]

random_list = [randrange(1, 10) for _ in range(20)]
print(random_list)
print(unic_value(random_list))