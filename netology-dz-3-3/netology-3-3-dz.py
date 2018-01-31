#coding: utf-8

import requests

def mut_friends(user_id1, user_id2):
    TOKEN = '---your toker hier---'

    params = {
        'access_token' : TOKEN,
        'source_uid' : user_id1,
        'target_uid' : user_id2
    }

    response = requests.get('https://api.vk.com/method/friends.getMutual', params)
    print('Идентификаторы общих друзей и ссылки на их страницы: ')
    for x, y in enumerate(response.json()['response'], 1):
        print(f"{x}. друг {y}. Ссылка на его страницу: https://vk.com/id{y}")


user_id1 = input('Введите id первого пользователя: ')
user_id2 = input('Введите id второго пользователя: ')
mut_friends(user_id1, user_id2)