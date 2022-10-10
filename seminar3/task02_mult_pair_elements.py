# Task 2
# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
from random  import math

def mult(numbers): # функция произведение парных элементов
    return [numbers[i] * numbers[-i - 1] for i in range(math.ceil(len(numbers)/2))]

n = list(input("Введите строку из чисел с разделителем в виде пробела: ").split(" "))
numbers = list(map(int, n))

print(numbers)
print(mult(numbers))

