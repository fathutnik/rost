#from django.shortcuts import render
import time
import vk
import requests
import json
from pyrogram import Client
try:
    result = json.loads(requests.get('http://193.124.117.173:8000/api/all?key=c21e9d9f7c68192ef79c2a6dddcbb953', timeout=90).text)
    ids = ''
    has_vk = list(filter(lambda x:x['vk_id']!='', result))
    for i in has_vk:
        ids += str(i['vk_id']) + ', '
    api = vk.API(session = vk.Session(access_token = ''))
    
    app = Client(
        'roctbb228bot',
        api_id=864763,  # your api_id
        api_hash='',
        proxy=dict(
            hostname="",
            port=,
            username="",
            password=""
        )
    )

    while True:
        print('sleep')
        #time.sleep(600 - (time.time() % 600))
        print('wake_up')
        t = time.time() - 600
        a = api.users.get(user_ids = ids[:-2], fields = 'online, last_seen', v = '5.92')
        ans = []
        for i in range(len(a)):
            if a[i]['online'] == 1 or a[i].get('last_seen', {'time': 0})['time'] > t:
                #api.messages.send(domain='agim3', message = '{}{}, {} домик, не спит в ВК'.format('*id' if str(has_vk[i]['vk_id']).isdigit() else '@', has_vk[i]['vk_id'], has_vk[i]['home_number'] if has_vk[i]['home_number'] != '' else 'n'), random_id = 0, v='5.92')
                app.send_message('fatnikita', 'vk.com/{}{}, {} домик, не спит в ВК'.format('id' if str(has_vk[i]['vk_id']).isdigit() else '', has_vk[i]['vk_id'], has_vk[i]['home_number'] if has_vk[i]['home_number'] != '' else 'n'))
        
        with app:
            members = [m for m in app.iter_chat_members(
                '-207970256')]

        for member in members:
            user = member.user
            if not user.is_bot and user.status.date > t:
                #api.messages.send(domain='agim3', message = '@{} не спит в TG'.format(user.username), random_id = 0, v='5.92')
                app.send_message('fatnikita', '@' + user.username + ' не спит в TG')
        break
except:
    print(0/0)
