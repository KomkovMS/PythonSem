"""
31. Сгенерировать файл из 10 строк, используя утилиту utils/gen_4_30.py. 
Написать программу, которая будет считывать сгенерированный файл построчно, 
складывать два числа и также построчно выводить результат сложения в stdout.

"""

# на семинаре
with open('data_4_30.txt', 'r') as fr:
    for i in fr:
        x, y = i.split()
        print(int(x) + int(y))

# пример решения на семинаре 5

"""import utils.gen_4_30 as utils

count_rows = 10
filename = 'file.txt'
n = 100

with open(filename, 'w', encoding='utf-8') as fw:
    for _ in range(count_rows):
        fw.write(f'{utils.get_double_args(n)}\n')

with open(filename, 'r', encoding='utf-8') as fr:
    for _ in range(count_rows):
        line = fr.readline()
        args = line.split(' ')
        print(int(args[0]) + int(args[1]))
"""
