"""
34. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):

a) Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.

  Например, число `19 ^ 3 = 6859` будем включать в сумму, так как `6 + 8 + 5 + 9 = 28` – делится нацело на `7`.  
Внимание: использовать только арифметические операции!

b) К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.

"""
# список из 500 элементов
# функция, которая раскладывает

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

# b)
res_b = 0
for j in arr:
	if sum_digits(j + 17) % 7 == 0:
		res_b += j
print(res_b)

# пример №1 решения на семинаре 5

"""def sum(n):
    sum = 0
    while (n != 0):
        sum += n % 10
        n = n // 10
    return sum

k = 0
for i in range(1, 1000, 2):
    num = i ** 3
    if sum(num) % 7 == 0:
        k += num

print(k)"""

"""def sum(n):
    sum = 0
    while (n != 0):
        sum += n % 10
        n = n // 10
    return sum

k = 0
for i in range(1, 1000, 2):
    num = i ** 3 + 17
    if sum(num) % 7 == 0:
        k += num

print(k)"""

# пример №2 решения на семинаре 5

"""
def check(number: int) -> bool:
    sum_of_digits = 0
    while number > 0:
        sum_of_digits += number % 10
        number //= 10

    return sum_of_digits % 7 == 0


if __name__ == "__main__":
    numbers = [i ** 3 for i in range(1, 1000, 2)]
    first_sum = 0
    second_sum = 0
    # тут я решил схитрить и посчитать обе суммы за один проход :)
    for number in numbers:
        if check(number):
            first_sum += number
        if check(number + 17):
            second_sum += number + 17

    print("Исходная сумма: {}".format(first_sum))               # Исходная сумма:                       17485588610
    print(f"Сумма чисел после увеличения на 17: {second_sum}")  # Сумма чисел после увеличения на 17:   15392909930
    """
