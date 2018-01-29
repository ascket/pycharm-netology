#coding: utf-8

import os
import subprocess

source = 'Source'
current_dir = os.path.dirname(os.path.abspath(__file__))
abs_file_dir = os.path.abspath(current_dir)
config_path = os.path.join(abs_file_dir, source)

file_list = []
for a in os.listdir(config_path):
    if a.endswith("jpg"):
        configs_path = os.path.join(abs_file_dir, source, a)
        configs_path_as = os.path.join(abs_file_dir, "Result", a)
        way = 'convert.exe', configs_path, 'convert -resize 200', configs_path_as
        way = ' '.join(way)
        file_list.append(way)

for i in file_list:
    repls = i.replace("\\", "\\\\")
    subprocess.Popen(repls)