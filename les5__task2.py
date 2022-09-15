"""
Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. 
Порядок элементов менять нельзя.

Пример:

[1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
"""

# на семинаре

# def get_list(lst: list, initial: int) -> list:
#     result = [lst[initial]]
#     for i in range(initial + 1, len(lst) - 1):
#         if result[-1] < lst[i]:
#             result.append(lst[i])
#     return result


# if __name__ == '__main__':
#     lst = [1, 5, 2, 3, 4, 6, 1, 7]
#     for i in range(len(lst)):
#         print(get_list(lst, i))

# на семинаре

def check(arr: list):
    s = [[[] for _ in range(len(arr))] for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr)):
            s[i][j].append(arr[i])
            for k in range(i + j + 1, len(arr)):
                if s[i][j][-1] < arr[k]:
                    s[i][j].append(arr[k])
                s[i].append(s[i][j].copy())
    return s


if __name__ == "__main__":
    source = [1, 5, 2, 3, 4, 6, 1, 7]

    r = check(source)
    result = set()
    for arr in r:
        for spam in arr:
            if len(spam) < 2:
                continue
            result.add(', '.join(map(str, spam)))

    for _ in result:
        print(_)
