"""
18. Реализуйте алгоритм перемешивания списка. 
(не использовать из модуля random метод `shuffle` другие методы допускается)
"""

import random

k = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print('current list: ', k)
shaker = []
for idx in range(len(k)):
	idx = random.randrange(len(k))
	shaker.append(k.pop(idx))
print('mixed list: ', shaker)






# k = [random.randint(-10,10) for s in range(10)]
# print(k)
# print('current list: ', k)

# def shaker(k):
#     first = 0
#     last = len(k) - 1


# shaker(k)

# print('mixed list: ', k)
