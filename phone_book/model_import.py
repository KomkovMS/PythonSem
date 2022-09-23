import model_rec


# 7 - импорт контакта в файл
def import_column(my_rec_book):
    with open('phone_book\phone_list.txt', 'a') as file:
        file.write(f'{my_rec_book[0]}\n{my_rec_book[1]}\n{my_rec_book[2]}\n{my_rec_book[3]}\n{"-"*80}\n')


def import_string(my_rec_book):
    with open('phone_book\phone_list.txt', 'a') as file:
        file.write(f'{my_rec_book[0]}; {my_rec_book[1]}; {my_rec_book[2]}; {my_rec_book[3]}\n{"-"*80}\n')
