# 4 - получение контакта 

def get_rec():
    my_rec_book = []
    last_name = input('Введите фамилию: ')
    my_rec_book.append(last_name)
    name = input('Введите имя: ')
    my_rec_book.append(name)
    phone = input('Введите телефонный номер: ')
    my_rec_book.append(phone)
    group = input('Введите описание контакта: ')
    my_rec_book.append(group)
    print('Вы ввели следующие данные: ', my_rec_book)
    return my_rec_book 
