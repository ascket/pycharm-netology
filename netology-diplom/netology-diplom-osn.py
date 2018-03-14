#coding: utf-8

import requests
import json


TOKEN = '5dfd6b0dee902310df772082421968f4c06443abecbc082a8440cb18910a56daca73ac8d04b25154a1128'

def api_vk(user_id, link):

    params_groups = {
        'access_token' : TOKEN,
        'user_id' : user_id,
        'v' : '5.73'
    }

    response_groups = requests.get(link, params_groups)
    groups_list = response_groups.json()['response']['items']
    return groups_list

ent_user_id = input('Введите userID: ')
groups_list = api_vk(ent_user_id, 'https://api.vk.com/method/groups.get')
friends_list = api_vk(ent_user_id, 'https://api.vk.com/method/friends.get')
print(groups_list)
print(friends_list)

groups_of_friends = []

for x in friends_list:
    try:
        groups_of_friends.append(api_vk(x, 'https://api.vk.com/method/groups.get'))
    except:
        #print('Пользователь удалён')
        continue


list_groups_of_friends = []

for n in range(0, len(groups_of_friends)):
    for jer in groups_of_friends[n]:
        list_groups_of_friends.append(jer)

sl_groups_of_friends = set(list_groups_of_friends)

list_osn = []

for i in groups_list:
    if i not in sl_groups_of_friends:
        list_osn.append(i)

#print(list_osn)

dict_groups = []

for i in list_osn:
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