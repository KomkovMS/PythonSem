from importlib.resources import path
import json
import pathlib


ROOT_DIR = pathlib.Path(__file__).parent.parent

print(ROOT_DIR)


data = {'test': 'test', 'text': 'Привет мир!', 'data': ['test', 'test', 'text', 'Привет мир!']}



with open(ROOT_DIR / 'dataset' / 'json_example_3.json', 'w', encoding='utf-8') as fw: # **
    json.dump(data, fw, ensure_ascii=False, indent=2)


with open(ROOT_DIR / 'dataset' / 'json_example_3.json', 'r', encoding='utf-8') as fr:
    dataset = json.load(fr)
    print(dataset, type(dataset))


# ** - когда не нужно проводить обработку данных со строкой