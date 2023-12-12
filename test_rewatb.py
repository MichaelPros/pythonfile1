def print_contacts(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        all_cont = file.readlines()
        if len(all_cont) != 0:
            for line in all_cont:
                print(line.strip(), end='\n\n')
        else:
            print('Список контактов пустой')

def connect_with_user():
    print('Введите имя, фамилию и телефон (например: Иван Иванов 89659679681): ')
    cont_info = input()
    return cont_info

def add_contact(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        all_cont = file.readlines()
    new_cont = connect_with_user()
    all_cont.append('\n' + new_cont)
    with open(file_name, 'w', encoding='utf8') as file:
        file.writelines(all_cont)

def find_contact(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        all_cont = file.readlines()

    print("Выберите критерий для поиска:" +
      '1 - Имя' +
      '2 - Фамилия' +
      '3 - Телефон'
      )

    comm = int(input())
    print('Введите строку для поиска:')
    data = input()
    print("Найденные контакты:")
    for cont in all_cont:
        cont_as_list = cont.strip().split()
        if data in cont_as_list[comm - 1]:
            print(*cont_as_list)

import shutil
def c_file(file_name, new_file_name):
    shutil.copy(file_name, new_file_name)

def copy_line_file(file_name, new_file):
    stroka = int(input('Введите номер строки: '))
    with open(file_name, 'r', encoding='utf8') as file:
        line_contact = file.readlines()
    if stroka > len(line_contact):
        print('Ведите количество строк с 0 до ' + str(len(line_contact)))
    else:
        copy_line = line_contact[stroka]
        with open(new_file, 'a', encoding='utf8') as f:
            f.writelines('\n'+ copy_line)
        print(f'Вы скопировали строку {stroka}!')

