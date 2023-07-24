from view import *

def write_name(name):
    with open("telefon.txt", "a", encoding="UTF-8") as file:
        file.write(name)

def search_smth_in_phone_book():
    number = input_search_option()
    look_world = input_want_to_find()
    with open("telefon.txt", "r", encoding="UTF-8") as file:
        lst = file.readlines()
        fnd_lst = []
        if number == 1:
            for row in lst:
                if row.split(',')[0] == look_world:
                    fnd_lst.append(row)
        if number == 2:
            for row in lst:
                if row.split(',')[1] == look_world:
                    fnd_lst.append(row)
        if number == 3:
            for row in lst:
                if row.split(',')[2] == look_world:
                    fnd_lst.append(row)
        return fnd_lst
 

def change_smth_in_phone_book():
    with open("telefon.txt", "r", encoding="UTF-8") as file:
        lst = file.readlines()
        print("Что нужно изменить?:")
        print(*search_smth_in_phone_book())
        id = input('Введите id удаляемого контакта: ')
        print('Введите новые данные: ')
        for i in range(len(lst)):
            if lst[i].split(',')[0] == id:
                lst[i] = id + "," + change_name_and_phone()    
    with open("telefon.txt", "w", encoding="UTF-8") as file:
        for row in lst:
            file.write(row)

def delete_smth_in_phone_book():
    with open("telefon.txt", "r", encoding="UTF-8") as file:
        lst = file.readlines()
        print("Вы хотите удалить?:")
        print(*search_smth_in_phone_book())
        id = input('Введите id удаляемого контакта: ')
        for i in range(len(lst)):
            if lst[i].split(',')[0] == id:
                lst[i] =''
    with open("telefon.txt", "w", encoding="UTF-8") as file:
        for row in lst:
            file.write(row)

def all_phone_book():
     with open("telefon.txt", "r", encoding="UTF-8") as file:
        lst = file.readlines()
        for row in lst:
            print(row)