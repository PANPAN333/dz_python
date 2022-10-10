# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random 

import itertools


num = int(input("Введите натуральную степень k: "))

def magic_to_file(num: int):
    if num > 0:
        with open('temp1.txt', "a", encoding="utf-8") as file:

            for i in reversed(range(1, num+1)):

                num1 = random.randint(0, 100)
                if num1 != 0:
                    print(f"{num1}*x^{i}+", file = file, end = " ")


            else:
                print(f"{num1} = 0", file = file)
magic_to_file(num)



def magic_to_file(num: int):
    if num > 0:
        with open('temp2.txt', "a", encoding="utf-8") as file:

            for i in reversed(range(1, num+1)):

                num1 = random.randint(0, 100)
                if num1 != 0:
                    print(f"{num1}*x^{i}+", file = file, end = " ")


            else:
                print(f"{num1} = 0", file = file)
magic_to_file(num)

