# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

import math

def is_prime(number):
    primes = [2]
    for num in range(3, number + 1, 2):
        if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
            primes.append(num)
    return primes

def get_prime_factors(number, primes): # функция получения простых множителей
    fact = []
    for i in primes:
        while number % i == 0:
            number = number / i
            fact.append(i)
    return fact

number = int(input('Введите число: '))

primes = is_prime(number)
factors = get_prime_factors(number, primes)
print(factors)
