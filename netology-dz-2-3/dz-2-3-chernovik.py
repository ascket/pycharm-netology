# coding: utf-8

import json
from pprint import pprint
import chardet as ch

with open("newsafr.json") as news:
    data = json.load(news)

pprint(data)