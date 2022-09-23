# 8 - экспорт контактов
def get_data_export():
    with open('phone_book\phone_list.txt', 'r') as file:
        for data in file:
            print(data)
