# import xlrd
# import random
#
# workbook = xlrd.open_workbook(r'D:\gos.xlsx')
# "workbook = xlrd.open_workbook(r'/content/drive/MyDrive/gos.xlsx')"
#
# worksheet = workbook.sheet_by_index(0)
# s = 0
# d = []
# lst = []
# for m in range(60):
#     p = random.randrange(0, 499, 1)
#     d.append(p)
# for i in d:
#     print(f'------------------\n {worksheet.cell_value(i, 0)} \n ')
#     print('Варианты ответ: \n')
#     for j in range(1, 5):
#         lst.append(f'{worksheet.cell_value(i, j)}')
#     random.shuffle(lst)
#     for t in range(len(lst)):
#         print(f'{t+1}){lst[t]}')
#     otvet = int(input('Введите номер ответа: '))
#     if lst[otvet - 1] == worksheet.cell_value(i, 1):
#         print('\n Вы ввели правильный ответ \n--------------------------')
#         s += 1
#     else:
#         print(f'\n Верный ответ: {worksheet.cell_value(i, 1)} \n--------------------')
#     lst = []
# print(f'Колличество верных ответов: {s}')




















