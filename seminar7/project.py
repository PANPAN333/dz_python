# создать телефонный справочник с возможностью импорта и экспорта данных

from datetime import datetime


def add(fio, number):
    with open('file.txt', 'a+', encoding='UTF-8') as file:
        file.write(f'{fio} | {number} | {datetime.now()}\n')

def readAll(showfile = 'file.txt'):
    with open(showfile, 'r', encoding='UTF-8') as file:
        lines = file.readlines()
        file.close()
        return lines

def displayScreen(data):
    data = [i.replace('|', '').rstrip('\n') for i in data]
    print()
    for i in range(len(data)):
        print(f"{i+1} {data[i]}")

def saveToTXT(data):
    data = [i.replace('|', '') for i in data]
    with open('export.txt', 'w+', encoding='UTF-8') as txt:
        for i in range(len(data)):
            txt.write(f"{i+1} {data[i]}")

_errors = ['Введите число!',
            'Значение не входит в диапазон.',
            'Не может быть равно 0!']

def input_numbers(str, not_null = False, a = None, b = None):
    flag = False
    tmp = None
    while(not flag):
        try:
            tmp = int(input(str))
            if a != None and b != None:
                if a <= tmp <= b:
                    flag = True
                else:
                    print(_errors[1])
            else:
                flag = True
            if not_null and tmp == 0:
                flag = False
                print(_errors[0])
        except:
            print(_errors[0])
    return tmp                                 

print('Телефонный Справочник\n'+
      '1. Посмотреть сохраненные записи\n'+
      '2. Добавить запись в справочник\n'+
      '3. Экспортировать в файл\n')
var = input_numbers('Выберите пункт меню: ',False,0,3)

match var:
    case 1:
        data = readAll()
        displayScreen(data)
    case 2:
        fio = input("Введите ФИО: ")
        number = input("Введите телефон: ")
        add(fio, number)
        print("Сохранено!")
    case 3:
        data = readAll()    
        saveToTXT(data)
        print("Сохранено!")  

