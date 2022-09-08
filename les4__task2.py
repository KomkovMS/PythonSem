"""
28. Найдите корни квадратного уравнения Ax² + Bx + C = 0, создав функцию для их нахождения. 
В качестве коэффициентов A, B и C для проверки работы функции передайте не менее трёх наборов данных, 
в одном из них коэффициент A = 0.
"""

# мое решение (по схеме решения кв. ур.)
import math
from multiprocessing.sharedctypes import Value

def get_quad_eq(a: int, b: int, c: int) -> int:
    d = b ** 2 - 4 * a * c
    if d < 0:
        x = print('нет действительных корней')
    elif d == 0:
        x = int(-1 * (b/(2 * a)))
        print((f'Ответ: один корень x = {x}'))
    else:
        x_1 = int(((-b) + math.sqrt(d)) / (2 * a)) # не решен вопрос с 0
        x_2 = int(((-b) - math.sqrt(d)) / (2 * a))
        x = print(f'Ответ: два корня x1 = {x_1}, x2 = {x_2}')


# get_quad_eq(3, -4, 2) # нет действительных корней
# get_quad_eq(1, -4, -5) # Ответ: два корня x1 = 5, x2 = -1
get_quad_eq(1, -6, 9) # Ответ: один корень x = 3


# на семинаре

def f(a, b, c):
    if a == 0:
        raise ValueError('Это не квадратное уровнение')
    diss = b ** 2 - 4 * a * c
    if diss < 0:
        return 'Корней нет'
    elif diss == 0:
        x = -b / (2 * a)
        return f'корень = {x}'
    else:
        x1 = (-b + diss ** 0.5) / (2 * a)
        x2 = (-b - diss ** 0.5) / (2 * a)
        return f'x1 = {x1}, x2 = {x2}'


print(f(2, 4, 7)) # Корней нет
print(f(1, -4, -5)) # x1 = 5.0, x2 = -1.0
print(f(1, -6, 9)) # корень = 3.0
print(f(0, 6, 9)) # ValueError: Это не квадратное уровнение
