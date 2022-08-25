"""
6. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
    
    *Пример:*
    
    - 6 -> да
    - 7 -> да
    - 1 -> нет


"""

def getDay(num: int) -> int:
    if num <= 0 or num > 7:
        input('enter a valid value from 1 to 7: ')
    if num < 6 and num > 0:
        print("нет")
    else:
        print("да")
    return num

num = getDay(int(input('Enter a number from 1 to 7: ')))