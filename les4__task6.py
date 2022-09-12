"""
32. Сгенерировать файл из чисел в диапазоне [-2, 2], используя утилиту utils/gen_4_30.py. 
Написать программу, считывающую все значения чисел из сгенерированного файла и выводящую в stdout только уникальные значения.

"""

def get_uniq_num(number):
    for num in number:
        if num not in unique:
            unique.append(num)
    return unique


with open('data_4_32.txt', 'r') as fr:  # 2 -2 1 2
    unique = []
    for i in fr:
        unique = get_uniq_num(list(i.split()))
        
print(' '.join(unique)) # 2 -2 1
