"""
14. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:

- 6782 -> 23
- 0,56 -> 11
"""

inp = input('enter number: ')
out = 0 
for num in range(len(inp)):
    if inp[num] not in ['.', ',']:
        out += int(inp[num])
print('sum = ', out)


# есть метод для дробных чисел в таком варианте?
# inp = float(input('enter number: '))
# out = 0
# while inp != 0:
#    	out = out + inp % 10
#    	inp = int(inp // 10)
# print(int(out))
