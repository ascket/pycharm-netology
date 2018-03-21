#coding: utf-8

import requests
import json
from time import sleep


TOKEN = '7b23e40ad10e08d3b7a8ec0956f2c57910c455e886b480b7d9fb59859870658c4a0b8fdc4dd494db19099'

def api_vk(user_id, link):
    sleep(0.1)

    params_groups = {
        'access_token' : TOKEN,
        'user_id' : user_id,
        'v' : '5.73'
    }

    response_groups = requests.get(link, params_groups)
    groups_list = response_groups.json()['response']['items']
    return groups_list

ent_user_id = input('Введите userID: ')
print('Шаг #1: получаем список групп пользователя...')
groups_list = api_vk(ent_user_id, 'https://api.vk.com/method/groups.get')
print('Список групп пользователя получен.')
print('Шаг #2: получаем список друзей пользователя...')
friends_list = api_vk(ent_user_id, 'https://api.vk.com/method/friends.get')
print('Список друзей пользователя получен')
print('Шаг #3: получаем список групп друзей пользователя...')

groups_of_friends = []

for x in friends_list:
    try:
        print('.')
        sleep(0.1)
        groups_of_friends.append(api_vk(x, 'https://api.vk.com/method/groups.get'))
    except:
        #print('Пользователь удалён')
        continue

print('Список групп друзей пользователя получен.')
print('Шаг #5: сравниваем списки...')

list_groups_of_friends = []

for n in range(0, len(groups_of_friends)):
    for jer in groups_of_friends[n]:
        print('.')
        list_groups_of_friends.append(jer)

sl_groups_of_friends = set(list_groups_of_friends)

list_osn = []

for i in groups_list:
    if i not in sl_groups_of_friends:
        list_osn.append(i)

print('Сравнивание списков завершено.')
print('Шаг #6: формируем и сохраняем файл со списком групп...')

dict_groups = []

for i in list_osn:
    sleep(0.1)
    dicter = {}
    params_groups = {
        'access_token': TOKEN,
        'group_id': i,
        'fields': 'members_count',
        'v': '5.52'
    }
    response_groups = requests.get('https://api.vk.com/method/groups.getById', params_groups)
    dicter['name'] = response_groups.json()['response'][0]['name']
    dicter['gid'] = response_groups.json()['response'][0]['id']
    dicter['members_count'] = response_groups.json()['response'][0]['members_count']
    dict_groups.append(dicter)

with open("groups.json", "w", encoding='utf-8') as pr:
    for data in dict_groups:
        json.dump(data, pr, indent=2, ensure_ascii=False)

print("Готово!")
