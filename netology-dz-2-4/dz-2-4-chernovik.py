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

def such_func(file, texter):
    selection = []
    for t in file:
        with open(os.path.join(config_path, t)) as ds:
            data = ds.read()
            if texter in data:
                selection.append(t)
    print(len(selection))
    return selection
    #print("Всего файлов {}".format(len(fert)))


while True:
    texter = input("Введите искомую фразу: ")
    print(such_func(file_list, texter))
