<<<<<<< HEAD
# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def input_numbers(x):
    xyz = ["x", "y", "z"]
    a = []
    for i in range(x):
        a.append(input(f"Введите значение {xyz[i]}: "))
    return a


def check_predicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] or not x[1]  or not x[2]
    result = left == right
    return result


statement = input_numbers(3)

if check_predicate(statement) == True:
    print("Утверждение истинно")
else:
=======
# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def input_numbers(x):
    xyz = ["x", "y", "z"]
    a = []
    for i in range(x):
        a.append(input(f"Введите значение {xyz[i]}: "))
    return a


def check_predicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] or not x[1]  or not x[2]
    result = left == right
    return result


statement = input_numbers(3)

if check_predicate(statement) == True:
    print("Утверждение истинно")
else:
>>>>>>> ed216bb3623851f1e0486abd73daaabd104c8174
    print("Утверждение ложно")