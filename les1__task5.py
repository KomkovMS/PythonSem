"""
Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

"""
# v1

num = int(input('Enter number'))
if (num % 5 == 0 and num % 10 == 0 or num % 15 == 0) and not num % 30 == 0:
    print("Введенное число ", num, " - кратно 5 и 10 или 15, но не 30")
else:
    print("Введенное число ", num, " - не соответствует условию")
