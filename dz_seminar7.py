# print_operation_table(operation, num_rows, num_columns)
#print_operation_table(lambda x, y: x * y, 3, 3)

num_rows = 3
num_columns = 3
# lst = []
# for i in range(1, num_columns + 1):
#     lst.append(i)
# print(lst)
# for i in range(1, num_rows):
#     for k in range(1, len(lst)):
#         lst[k] = lst[k] * lst[i]
#         lst[0] = k
#     print(lst)
lst = []
for i in range(1, num_columns + 1):
    lst.append(str(i))
lst1 = ' '.join(lst)
for j in range(2, num_rows + 1):

    operation = lambda x, y: x * y

print(operation(i,i))
print(lst)
print(lst1)
print(type(lst[0]))
print(type(lst[1]))