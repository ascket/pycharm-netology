#coding: utf-8

import os

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))
abs_file_dir = os.path.abspath(current_dir)
config_path = os.path.join(abs_file_dir, migrations)

file_list = []
for i in os.listdir(config_path):
    if i.endswith("sql"):
        file_list.append(i)

def such_func():
    texter = input("Введите искомую фразу: ")
    selections = []
    for t in file_list:
        with open(os.path.join(config_path, t)) as ds:
            data = ds.read()
            if texter in data:
                selections.append(t)
    print('\n'.join(selections))
    print("Всего файлов: ", len(selections))
    return selections

such_func()

while True:
    file_list = such_func()
