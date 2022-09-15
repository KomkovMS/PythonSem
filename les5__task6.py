"""
40. *Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

Пример:
AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
6A1F2D7C1A17E
"""

# модуль сжатия

with open('PythonSem\les5_task6.md', mode='r', encoding='utf-8') as f:
    my_txt = f.read()

def get_compression(my_txt):
    compression = ''  
    letter = ''  
    total = 1
    for item in my_txt:
        if item != letter:
            if letter:
                compression += str(total) + letter
            total = 1
            letter = item
        else:
            total += 1
    return compression

            
compression = get_compression(my_txt)

with open('PythonSem\les5__task6_output.md', mode='w', encoding='utf-8') as f:
    f.write(compression)

# print(compression)

# модуль восстановления данных

with open('PythonSem\les5__task6_output.md', mode='r', encoding='utf-8') as f:
    my_txt = f.read()

def get_recovery(my_txt):
    total = ''
    recovery = ''
    for item in my_txt:
        if item.isdigit():
            total += item 
        else:
            recovery += item * int(total)
            total = ''
    return recovery


recovery = get_recovery(my_txt)
with open('PythonSem\les5__task6__rec.md', mode='w', encoding='utf-8') as f:
    f.write(recovery)
