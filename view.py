from database import *

def input_number():
    answer= int(input("Выберете действие:\n1-записать нового пользователя\n2-вывести телефонный справочник\n3-найти\n4-изменить\n5-удалить\n0-закончить работу\n"))
    return answer

def add_name_and_phone():
    id = '1'
    with open("telefon.txt", "a", encoding="UTF-8") as file:
        lst = file.readlines()
        lst.sort(key= lambda x: int(x.split(',')[0]))
        for row in lst:
            if row.split(',')[0] == id:
                id = str(int(id) + 1) 
    name = input('Введите имя: ')
    surname = input('Ввелите фамилию: ')
    tel = input('Введите номер телефона: ')
    res = id + "," + name + "," + surname + ',' + tel + '\n' 
    return res

def input_search_option():
    search_option = int(input('Выберите вариант поиска: \n 1 - id \n 2 - имя \n 3 - фамилия \n'))
    return search_option

def input_want_to_find():
    char = input("Введите слово поиска:\n")
    return char

def change_name_and_phone():
    name = input('Введите имя: ')
    surname = input('Ввелите фамилию: ')
    tel = input('Введите номер телефона: ')
    res =name + "," + surname + ',' + tel + '\n' 
    return res