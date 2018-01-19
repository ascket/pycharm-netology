#coding: utf-8

import os

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))
abs_file_dir = os.path.abspath(current_dir)
config_path = os.path.join(abs_file_dir, migrations)
file_list = []
for i in os.listdir(config_path):
    if ".sql" in i:
        file_list.append(i)

while True:
    def opens():
        fert = []
        texter = input("Введите: ")
        for t in file_list:
            with open(os.path.join(config_path, t)) as ds:
                data = ds.read()
                if texter in data:
                    fert.append(t)
        print(fert)
        print("Всего файлов {}".format(len(fert)))


    opens()