"""
25. *Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

45 -> 101101
3 -> 11
2 -> 10

...
"""


def get_num(num, n):
    while num > 0:
        y = str(num % 2)
        n = y + n
        num = int(num / 2)
    return n

num = int(input('enter a number: '))
n = ''
print(get_num(num, n))