"""
Домашнее задание:

37. *Напишите программу, удаляющую из текста все слова, содержащие "абв".
Входные и выходные данные хранятся в отдельных текстовых файлах.

"""

# my_str = 'Хочу поехать в Зимбабве. "Абв" - первые буквы алфавита'

with open('PythonSem\les5_task3_input.md', mode='r', encoding='utf-8') as f:
    my_str = f.read()
    result = ' '.join(filter(lambda x: 'абв' not in x, my_str.lower().split()))
    # print(result)
with open('PythonSem\les5_task3_output.md', mode='w', encoding='utf-8') as f:
     f.write(result)
