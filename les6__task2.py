"""
42. Дана последовательность чисел. Получить отсортированный по возрастанию список уникальных элементов заданной последовательности.

Пример:

[1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

"""

# моe решение:
"""def get_uniq_num(number):
    for num in number:
        if num not in val and num.isdigit():
            val.append(num)
    return sorted(list(val))


my_list = '1, 2, 3, 5, 1, 5, 3, 10'
val = []
for i in my_list:
    val = get_uniq_num(list(i.split()))
        
print(', '.join(val)) # 0, 1, 2, 3, 5"""


# на семинаре

def sort_lst(lst: list) -> list:
    """ возвращаем отсортированные уникальные значения """
    uniq_elements = set()
    for el in lst:
        if el not in uniq_elements:
            uniq_elements.add(el)
        else:
            uniq_elements.discard(el)

    s = list(uniq_elements)
    # return sorted(s) или:
    s.sort()
    return s


if __name__ == "__main__":
    lst = [1, 2, 3, 5, 1, 5, 3, 10]
    print(sort_lst(lst))  # [2, 10]
