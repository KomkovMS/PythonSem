# списки, множества
ll = (1, 2, 3, 4, 1, 4)
print(list(ll))
s = set(ll)     #set - множество
l = list(ll)    #list - список
print(l)
print(s)
# help(list), help(set) - просмотреть все методы списка, множества (+ словарь - объекты изменяемого типа)
# list чаще всего используют как объект иттерируемого типа
# frozenset - неизменяемое множество
print(frozenset(ll))
# help(frozenset.add) - нет такого метода, относится к неизменяемому типу