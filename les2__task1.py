"""
11. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
    
    *Пример:*
    
    - Для N = 5: 1, -3, 9, -27, 81

"""

x = int(input())
k = 1
for i in range(1, x + 1):
    print(k, end=', ') 
    k *= -3

# x = 5
# k = 1
# i = 0
# x = 1
# print(k) //  1
# k = 1 * -3 = -3
# i = 1
# x = 2
# print(k) // -3
# k = - 3 * - 3
# i = 2
# x = 2 + 1 = 3
# print(k) // -3 * -3 = 9
# k = 9 * -3 = - 27
# i = 3
# x = 3 + 1 = 4
# print(k)  // -27
# k = -27 * -3  // 81
# i = 4
# x = 4 + 1 = 5
# print(k)  // 81

num = int(input('\n'))
k = 1
for i in range(0, num):
    print(k, end=', ')
    k *= -3