"""
27. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.

"""

# мое решение
my_list = [2, 45, 54, 3, 12, 0, 7, -3, 12, -65, 4, 23]
max_num, min_num = max(my_list), min(my_list)
print(f'Большее: {max_num} и меньшее: {min_num}')

# на семинаре
def max_min(arr: list) -> int:
    max_num = arr[0]
    min_num = arr[0]
    for i in range(1, len(arr)):
        if max_num < arr[i]:
            max_num = arr[i]
        if min_num > arr[i]:
            min_num = arr[i]
    return max_num, min_num


my_list = '2 45 54 3 12 0 7 -3 12 -65 4 23'.split(' ')
for i in range(len(my_list)):
    my_list[i] = int(my_list[i])

max_num, min_num = max_min(my_list)
print(f'Большее: {max_num} и меньшее: {min_num}')



