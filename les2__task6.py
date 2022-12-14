"""
16. Задайте список из n чисел последовательности (1 + 1/n) ** n
 
 и выведите на экран их сумму.

Пример:
Для n = 6 
Подсказка: округление значений можно сделать через round(..., 2)
"""

num = int(input('Enter number: '))

result = 0
for idx in range(1, num + 1):
    result += ((1 + 1/idx) ** idx)

print('Сумма последовательности n чисел: ', round(result, 3))

