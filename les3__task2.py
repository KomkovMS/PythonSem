"""
20. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число

"""

x = ['2', '5', '4', '8', 'hello', 'hi-6']
app = input('Enter number: ')
flag = False

for i in x:
    if app in i:
        flag = True
        break

if flag:
    print('Значение в списке')
else: 
    print('Значения нет в списке')

