print('я пример первого %d формата %s' % (123, 666))
print('я пример второго {1} формата {0}'.format(111 + 444, 666))
print('я вариация второго {first} формата {second}'.format(first='555', second=666))
print(f'я пример третьего формата {100 + 11}')

# самый медленный
print('я самый ' + str(555) + ' медленный')  # конкатенация строк