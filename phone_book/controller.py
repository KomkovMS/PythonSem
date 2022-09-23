import views
import model_export
import model_import
import model_rec


# 5 - обработка операции выбора импорта или экспорта данных
# 6 - обработка операции выбора формата записи
def processing_action_choice():
    welcom = views.get_welcom()
    action_choice = views.get_action_choice()
    if action_choice == 1:
        print(f'Вы выбрали импорт (внесение нового контакта)')
        form = views.get_choose_rec_format()
        if form == 1:
            print(f'Вы выбрали формат записи в столбик')
            model_import.import_column(model_rec.get_rec())
        else: 
            print(f'Вы выбрали формат записи в строку')
            model_import.import_string(model_rec.get_rec())
    else: 
        print(f'Вы выбрали экспорт (печать телефонного справочника)')
        model_export.get_data_export()
