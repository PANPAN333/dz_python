# Task 1
# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def sum(numbers): # функция суммы нечетных позиций
    return sum(numbers[1::2])

n = list(input("Введите строку из чисел с разделителем в виде пробела: ").split(" "))
numbers = list(map(int, n))
l = len(numbers)
print(numbers)
print(sum(numbers))

