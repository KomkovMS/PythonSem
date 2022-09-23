"""
44. Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования.

main - точка запуска
view - взаимодействие с пользователем
model - модели, переменные, данные
controller - связка view и model для решения конкретной задачи

Рационáльное числó («отношение, деление, дробь») — число, которое можно представить в виде обыкновенной дроби m/n, 
где m — целое число, а n — натуральное. 
Ко́мпле́ксные чи́сла (связь, сочетание) — числа вида a + bi где a,b — вещественные числа, i — мнимая единица, 
то есть число, для которого выполняется равенство: a + 0i
"""

from operator import add, sub, mul, truediv


# получение данных от пользователя - view
def get_rational() -> str:
    return input("Введите выражение (example: 6/10+1.5): ")


def get_complex() -> str:
    pass


# выбор типа чисел для работы -> view
def show_menu() -> str:
    result = input('Выберите тип чисел для работы (Q - рациональные, C - комплексные): ')
    return result.upper()


def operation(a: float, op: str, b: float) -> list:
    """Считывает арифметические операции для двух чисел и вернет 
    округленный результат"""
    opers = {'+': add, '-': sub, '*': mul, '/': truediv}
    callback = opers.get(op)
    if not callback:
        raise ArithmeticError('operator unknown')
    return round(callback(a, b), 2)


# разбор ввода пользователя
def calculate(lst: list) -> float:
    result = 0.0
    for s in '*/+-':
        while s in lst:
            index = lst.index(s)
            result = operation(lst[index - 1], s, lst[index + 1])
            lst = lst[:index - 1] + [result] + lst[index + 2:]
    return result


def parse(s: str) -> list:
    result = []
    digit =''
    for symbol in s:
        if symbol.isdigit() or symbol == '.':
            digit += symbol
        elif symbol in [')', '(']:
            if digit:
                result.append(float(digit))
                digit = ''
            result.append(symbol)
        else:
            if digit:
                result.append(float(digit))
            digit = ''
            result.append(symbol)
    else:
        if digit:
            result.append(float(digit))
    return result


# вывод результата
def show_result(result: float):
    print(f'Результат вычислений {result: .2f}')


# controller (получить, посчитать, отдать)
def process_data():
    number_type = show_menu()
    if number_type == 'Q':
        user_input = get_rational()
    else:
        user_input = get_complex()
    data = parse(user_input)
    result = calculate(data)
    show_result(result)


def main():
    process_data()


if __name__ == '__main__':
    main()
