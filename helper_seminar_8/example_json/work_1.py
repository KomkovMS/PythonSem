from asyncore import read
import json
import pathlib
from tkinter import W


ROOT_DIR = pathlib.Path(__file__).parent.parent

print(ROOT_DIR)


data = {'test': 'test', 'text': 'Привет мир!', 'data': ['test', 'test', 'text', 'Привет мир!']}
dataset = [{'test': 'test', 'text': 'Привет мир!', 'data': {'test': 'test', 'text': 'Привет мир!'}} for _ in range(10)]

# json_str = json.dumps(data, ensure_ascii=False, indent=2)
with open(ROOT_DIR / 'dataset' / 'json_example_1.json', 'w', encoding='utf-8') as fw:
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    fw.write(json_str)
    print(type(json_str))

with open(ROOT_DIR / 'dataset' / 'json_example_1.json', 'r', encoding='utf-8') as fr:
    data_str = fr.read()
    dataset = json.loads(data_str)
    print(dataset, type(dataset))


# json_str = json.dumps(dataset, ensure_ascii=False, indent=2)
# with open(ROOT_DIR / 'dataset' / 'json_example_2.json', 'w', encoding='utf-8') as fw:
#     fw.write(json_str)

# ensure_ascii=False - отображение кириллицы
# indent=2 - отступ
# son.dumps - делает строку
# json.loads -обратно вернул объект питона
