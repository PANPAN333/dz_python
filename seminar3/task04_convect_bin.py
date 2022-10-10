# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def convect(number):
    bin_num = ''
    while number > 1:
        bin_num += str(number % 2)
        number = number // 2
    return bin_num[::-1]

number = int(input('Введите число: '))
print(convect(number))
