#coding: utf-8

import osa
import os
import math

files = 'Files'
current_dir = os.path.dirname(os.path.abspath(__file__))
abs_file_dir = os.path.abspath(current_dir)
config_path = os.path.join(abs_file_dir, files)

with open(os.path.join(config_path, "temps.txt")) as myfile:
    temperature = []
    data = myfile.read()
    fields = data.split()
    temperature = fields[::2]

client = osa.Client('http://www.webservicex.net/ConvertTemperature.asmx?WSDL')

average_celsius = 0
for ah in temperature:
    average_celsius += client.service.ConvertTemp(int(ah), 'degreeFahrenheit', 'degreeCelsius')

print("Средняя температура в градусах Цельсия:", average_celsius/len(temperature))


print("--------------")


with open(os.path.join(config_path, "currencies.txt")) as curla:
    data = curla.read()
    fields = data.split()

client = osa.Client('http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL')

for i in range(2, len(fields) + 2, 3):
    print(fields[i-2], math.ceil(client.service.ConvertToNum('', fields[i], 'RUB', fields[i-1], '', '', '')), "рублей")


print("--------------")


with open(os.path.join(config_path, "travel.txt")) as travel:
    data = travel.read()
    fields = data.split()

client = osa.Client('http://www.webservicex.net/length.asmx?WSDL')

for i in range(2, len(fields) + 2, 3):
    print(fields[i-2], round(client.service.ChangeLengthUnit(fields[i-1].replace(",", ""), 'Miles', 'Kilometers'), 2), "километров")
