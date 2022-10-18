import math

def mult(numbers): # функция произведение парных элементов
    return [numbers[i] * numbers[-i - 1] for i in range(math.ceil(len(numbers)/2))]

n = list(input("Введите строку из чисел с разделителем в виде пробела: ").split(" "))
numbers = list(map(int, n))

print(numbers)
print(mult(numbers))

