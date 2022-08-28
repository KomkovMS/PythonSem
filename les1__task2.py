"""
2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

Примеры:

1, 4, 8, 7, 5 -> 8
78, 55, 36, 90, 2 -> 90


"""
# var1 

num1 = int(input('Enter first number'))
num2 = int(input('Enter first number'))
num3 = int(input('Enter first number'))
num4 = int(input('Enter first number'))
num5 = int(input('Enter first number'))

max = num1

if max < num2:
    max = num2
if max < num3:
    max = num3
if max < num4:
    max = num4
if max < num5:
    max = num5

print('max =', max)

# var2

def getMaxNum(arr):
    max = arr[0]
    for i in arr:
        if i > max:
            max = i
    return max

arr = [num1, num2, num3, num4, num5]
print('Так тоже максимальное число будет ', getMaxNum(arr))

# var3 - оптимально
max = 0
for _ in range(5):
    num = int(input('Enter first number'))
    if num > max:
        max = num

print(f'max={max}')
