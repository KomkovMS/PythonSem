import csv
import pathlib


ROOT_DIR = pathlib.Path(__file__).parent.parent

with open(ROOT_DIR / 'dataset' / 'cvs_example_1.cvs', 'w', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=',')
    csv_writer.writerow(['Данил', 'Глеб', 'Анастасия', 'Максим', 'Анатолий']) # может быть кортеж, ключи словаря, 
    csv_writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam']) 
    csv_writer.writerow([str(_) for _ in range(1, 6)]) 


with open(ROOT_DIR / 'dataset' / 'cvs_example_2.cvs', 'w', encoding='utf-8') as csvfile:
    fieldnames = ['id', 'first_name', 'second_name', 'last_name']
    csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    csv_writer.writeheader()
    for i in range(1, 11):
        csv_writer.writerow(
            {'id': i, 'second_name': f"отчество_{i}",
            'first_name': f"имя_{i}", 'last_name': f"фамилия_{i}"}
        )
        
    # csv_writer.writerow({'id': 11, 'second_name': "Иванович",
    #                      'first_name': "Иван",
    #                      'last_name': "Иванов"})


# delimiter=' ' -разделиртель между данными в одной строке
# csv.writer - возвращает класс writer
# writerow - запиши в себя такую-то строчку