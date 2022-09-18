"""
34. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):

a) Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.

  Например, число `19 ^ 3 = 6859` будем включать в сумму, так как `6 + 8 + 5 + 9 = 28` – делится нацело на `7`.  
Внимание: использовать только арифметические операции!

b) К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.

"""

def sum_digits(value):
    res = 0
    while value != 0:
        res += value % 10
        value //= 10
    return res


arr = [i**3 for i in range(1, 1000, 2)]

# a)
res_a = 0
for i in arr:
	if sum_digits(i) % 7 == 0:
		res_a += i
print(res_a)

# 1.1 Выражение-генератор, функция sum() складывает содержимое генератора
print(sum(i for i in arr if sum_digits(i) % 7 == 0))  
# 1.2 List Comprehension 
print(sum([i for i in arr if sum_digits(i) % 7 == 0]))
# 1.3 Set Comprehension
print(sum({i for i in arr if sum_digits(i) % 7 == 0}))
# 2 Filter, lambda
print(sum(filter(lambda i: sum_digits(i) % 7 == 0, arr)))
# 3 Map, lambda
print(sum(map(lambda i: i if sum_digits(i) % 7 == 0 else 0, arr)))
# 


# b)
res_b = 0
for j in arr:
	if sum_digits(j + 17) % 7 == 0:
		res_b += j
print(res_b)
#
print(sum(j for j in arr if sum_digits(j + 17) % 7 == 0))  
print(sum([j for j in arr if sum_digits(j + 17) % 7 == 0]))
print(sum({j for j in arr if sum_digits(j + 17) % 7 == 0}))
print(sum(filter(lambda j: sum_digits(j + 17) % 7 == 0, arr)))
print(sum(map(lambda j: j if sum_digits(j + 17) % 7 == 0 else 0, arr)))