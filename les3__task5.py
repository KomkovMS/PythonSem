"""
23. *Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

[2, 3, 4, 5, 6] => [12, 15, 16];
[2, 3, 5, 6] => [12, 15]

нечетный список - 
срез, обращение по индексу к 1 элементу и последнему, 
изменение списка
"""


my_list = [2, 3, 4, 5, 6]
# my_list = [2, 3, 5, 6]
new_list = []
middle = None

if len(my_list) % 2 != 0:
    middle = 1
else:
    middle = 0
start = int(len(my_list) / 2 + middle)

for num in range(start):
    arg_1 = my_list[num]
    # print(my_list[num])
    arg_2 = my_list[-(num+1)]
    # print(my_list[-(num+1)])
    result = arg_1 * arg_2
    new_list.append(result)
    
# print(start)
print(f'Произведение пар чисел списка {my_list} по условию задачи: {new_list}')

