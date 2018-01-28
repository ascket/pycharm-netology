#coding: utf-8

import requests
import chardet as ch
import os

def translate_it(text, language):
    """
    YANDEX translation plugin
    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20180124T171800Z.e9a6541121358b50.63eb5863bf2f73ee678d7671177572facf8f918c'

    params = {
        'key': key,
        'lang': language.lower() + "-ru",
        'text': text,
    }
    response = requests.get(url, params=params).json()
    return ' '.join(response.get('text', []))

def files():
    source = 'Files'
    current_dir = os.path.dirname(os.path.abspath(__file__))
    abs_file_dir = os.path.abspath(current_dir)
    config_path = os.path.join(abs_file_dir, source)

    file_list = []
    for all_files in os.listdir(config_path):
        if all_files.endswith("txt"):
            configs_path = os.path.join(abs_file_dir, source, all_files)
            file_list.append(configs_path)
    return file_list

def full_translate():
    for elem in files():
        with open(elem, "rb") as news:
            data = news.read()
            result = ch.detect(data)
            full_text = data.decode(result["encoding"])
            lang = os.path.splitext(os.path.basename(elem))[0] #берёт только название файла без расширения
            translate_func = translate_it(full_text, lang)
        with open(lang + "-translate.txt", "w") as rs:
            rs.write(translate_func)

full_translate()