# Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.
# Для k  = 6: {1: 4, 2: 7, 3: 10, 4:13, 5: 16, 6:19}
k = int(input("Введите число: "))

list = []
i = 0
for i in range(k):
    list.append(float(1 + 1 / k) ** k)
    i += 1

print(sum(list))
