"""
В файле находится N натуральных чисел, записанных через пробел. 
Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. 
Найдите это число.
"""

# на семинаре:

import random


mas = [i for i in range(1, 11)]
print(mas)

idx = random.randint(0, 9)
print(idx)
del mas[idx]
print(idx, mas)

for i in range(1, len(mas)):
    if mas[i] - 1 != mas[i - 1]:
        mas.insert(i, mas[i - 1] + 1)
        break
print(mas)
