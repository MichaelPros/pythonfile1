from test_rewatb import *

CONTACTS = 'contacts.txt'
CONTACTSCOPY = 'contactscopy.txt'
CONTACTSCOPY1 = 'contactscopy1.txt'


def interface():
    while True:
        print('Выберете действие:\n' +
              '1 - Добавить контакт\n' +
              '2 - Вывести все контакты\n' +
              '3 - Найти контакт\n' +
              '4 - Копировать файл\n' +
              '5 - Скопировать строку в файле\n' +
              '0 - Выйти')
        kommand = int(input())
        match kommand:
            case 0:
                break
            case 1:
                add_contact(CONTACTS)
            case 2:
                print_contacts(CONTACTS)
            case 3:
                find_contact(CONTACTS)
            case 4:
                c_file(CONTACTS, CONTACTSCOPY)
            case 5:
                copy_line_file(CONTACTS, CONTACTSCOPY1)
            case _:
                print("Не верная команда!")


if __name__ == '__main__':
    interface()
