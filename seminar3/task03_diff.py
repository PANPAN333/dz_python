# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# # - [1.1, 1.2, 3.1, 5, 10.01] => 0.19



from random import random


def find_diff(numbers):
    nums = [round(x - int(x), 2) for x in (numbers)]
    return max(nums) - min(nums)


n = list(input("Введите строку из чисел с разделителем в виде пробела: ").split(" "))
numbers = list(map(float, n))

print (numbers)
print(find_diff(numbers))


