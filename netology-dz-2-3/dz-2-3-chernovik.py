# coding: utf-8

#import json
import chardet as ch

with open("newscy.json", "rb") as news:
    data = news.read()
    result = ch.detect(data)
    full_text = data.decode(result["encoding"])
    #fields = full_text.split()
    print(result)

    print(full_text)