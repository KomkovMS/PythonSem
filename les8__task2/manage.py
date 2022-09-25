from importlib.resources import path
import json
import pathlib
import CRUD


ROOT_DIR = pathlib.Path(__file__).parent.parent


def read_file(file_name: str) -> list:
    with open(file_name, 'r', encoding='utf-8') as fr:
        json_str = fr.read()
        dataset = json.loads(json_str)
        return dataset

# print(read_file(ROOT_DIR / 'les8__task2' / "api.json"))

def write_file(dataset: list, file_name: str) -> str:
    with open(file_name, 'w', encoding='utf-8') as fw:
        json_str = json.dumps(dataset, ensure_ascii=False, indent=2)
        fw.write(json_str)
        return json_str


lst = read_file(ROOT_DIR / 'les8__task2' / "api.json")
write_file(lst, ROOT_DIR / 'les8__task2' / "api.json")