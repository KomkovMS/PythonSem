# 1 - приветствие
def get_welcom():
    welcom = 'Добро пожаловать в телефонную книгу!'
    return print(welcom)


# 2 выбор импорта или экспорта данных 
def get_action_choice():
    action_choice = int(input('Введите операцию c контактами: 1 - импорт или 2 - экспорт? '))
    return action_choice


# 3 - выбор формата записи
def get_choose_rec_format():
    form = int(input('Выберите формат записи: 1 - в столбик, 2 - в строку -> '))
    return form
