"""
3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

Примеры:

5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

"""

# var 1

x = int(input())
for i in range(-x, x + 1):
    print(i, end = ", ")

# var 2

def f(n):
    for i in range(-n, n + 1):
        print(i, end=', ')
res = int(input())


f(res)
