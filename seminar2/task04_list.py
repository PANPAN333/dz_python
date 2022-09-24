# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.
import random

random_list = random.sample(range(-10, 10), 10)
for i, ii in enumerate(random_list):
    print(random_list[i], end=' ')

c = list(map(int,input('Введите значения элементов: ').split()))
try:
    print(random_list[c])
except Exception as exc:
    print(exc)


prod = 1
for i in c:
    prod *= i
print(f'Весь список: {random_list}')
print(f'Произведение элементов списка {c}: {prod}')

