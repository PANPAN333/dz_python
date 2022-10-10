# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

def get_fibonacci(number):
    fib_numbers = []
    a, b = 1, 1
    for i in range(number-1):
        fib_numbers.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (number):
        fib_numbers.insert(0, a)
        a, b = b, a - b
    return fib_numbers


number = int(input('Введите число: '))
fib_numbers = get_fibonacci(number)
print(get_fibonacci(number))

