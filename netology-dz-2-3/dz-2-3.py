# coding: utf-8

import json
import pprint
import chardet as ch


def words_count(article):
    with open(article, "rb") as news_code:
        file_read = news_code.read()
        result = ch.detect(file_read)
        file_code = result["encoding"]
    with open(article, encoding=file_code) as news:
        data = json.load(news)
        full_text = pprint.pformat(data)
        fields = full_text.split()

        long_words = []
        for words in fields:
            alfa = len(words)
            if alfa > 6:
                long_words.append(words.lower())

        words_with_count = {}
        for words in long_words:
            words_with_count.setdefault(words, 0)
            words_with_count[words] += 1

        count_list = []
        for value in words_with_count.values():
            if value not in count_list:
                count_list.append(value)
        beta = sorted(count_list)
        count_list_reverse = beta[::-1]

        count_list_reverse_lim = count_list_reverse[:10]

        for elementen in count_list_reverse_lim:
            for key, values in words_with_count.items():
                if words_with_count[key] == elementen:
                    print('Слово "{}" встречается {} раз(а)'.format(key, values))


def main():
    global article
    while True:
        article_number = input('Статьи:\n[1] = newsafr.json\n'
                               '[2] = newscy.json\n'
                               '[3] = newsfr.json\n'
                               '[4] = newsit.json\n'
                               'Введите номер статьи или любую другую кнопку для выхода: ')
        if article_number == "1":
            article = "newsafr.json"
        elif article_number == "2":
            article = "newscy.json"
        elif article_number == "3":
            article = "newsfr.json"
        elif article_number == "4":
            article = "newsit.json"
        else:
            break
        print("Топ 10 наиболее часто встречающихся слов длиннее 6-ти символов:")
        words_count(article)


main()
