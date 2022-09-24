<<<<<<< HEAD
# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

def check_zone(chetv):
    match chetv:
        case 1 :
            print("x > 0 and y > 0")
        case 2:
            print(" x < 0 and y > 0")
        case 3:
            print("x < 0 and y < 0")      
        case 4:
            print("x > 0 and y < 0")

input_zone = int(input("Введите номер четверти: "))
check_zone(input_zone)





=======
# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

def check_zone(chetv):
    match chetv:
        case 1 :
            print("x > 0 and y > 0")
        case 2:
            print(" x < 0 and y > 0")
        case 3:
            print("x < 0 and y < 0")      
        case 4:
            print("x > 0 and y < 0")

input_zone = int(input("Введите номер четверти: "))
check_zone(input_zone)





>>>>>>> ed216bb3623851f1e0486abd73daaabd104c8174
