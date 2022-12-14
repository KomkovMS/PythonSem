"""
13. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.
"""

def search(source: str, research: str) -> int:
    s_1 = source.lower()
    s_2 = research.lower()
    return s_1.count(s_2)

if __name__ == '__main__':
    s1 = input('Введите большую строку: ')
    s2 = input('Введите искомую строку: ')
    print(f'Найдено вхождений: {search(s1, s2)}')


# Функция Index - это встроенный метод списка, который позволяет узнать индекс или позицию элемента в последовательности.  
# этот метод ищет элемент в списке и возвращает его индекс
# S.count(str, [start],[end]) Возвращает количество непересекающихся вхождений подстроки в диапазоне [начало, конец] 
# (0 и длина строки по умолчанию)
# S.lower() - Преобразование строки к нижнему регистру

# Строки. Функции и методы строк https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html
