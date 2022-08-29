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
