"""
1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
Примеры:

5, 25 -> да
4, 16 -> да
25, 5 -> да
8,9 -> нет

"""

def check(a: int, b :int) -> bool:
    if a > b:
        a, b = b, a
    return a ** 2 == b

def f_sum(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    result = check(int(input('Enter first number: ')),
          int(input('Enter second number ')))
    print(f'Одно число является квадратом другого: {"yes" if result else "no"}')