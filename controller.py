
from view import *
from database import *

def main():
    while True:
        num = input_number()
        if num == 1:
            res = add_name_and_phone()
            write_name(res)
            print('Успешно записано\n')
        if num == 2:
            print('Телефонный справочник:\n')
            all_phone_book()    
        if num == 3:
            print(*search_smth_in_phone_book())
            print('Успешно найдено\n')
        if num == 4:
            change_smth_in_phone_book()
            print('Успешно изменено\n')
        if num == 5:
            delete_smth_in_phone_book()
            print('Успешно удалено\n')
        if num == 0:
            break

main()
