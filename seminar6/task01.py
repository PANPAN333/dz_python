str = "пара-ра-рам рам-пам-папам па-ра-па-дам".split()


rez = [sum(x in 'а вы шо ожидали здесь прочитать' for x in i) for i in str]

if len(set(rez)) == 1: # именно == 1
    print("Та дам") 
else: 
    print("Тудумс")