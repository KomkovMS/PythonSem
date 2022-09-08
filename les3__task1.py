"""
19. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

"""

import random
import time

x = random.randint(1, 100)
print(x)

#var.1 на уроке
def get_rand(x: int, y: int) -> int:
    if x > y:
        raise ValueError("Ошибка! x должен быть меньше y")
    scope = y - x
    result = int(time.time()) % scope
    return result + x


if __name__ == "__main__":
    print(get_rand(1, 100))


#var.2
the_set = set()

for i in range(101):
    the_set.add(str(i))

for e in the_set:
    print(int(e))
    break