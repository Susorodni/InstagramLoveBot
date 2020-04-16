#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password
import pickle
import time
import random
from InstagramAPI import InstagramAPI
import datetime


api = InstagramAPI.InstagramAPI("username", "password")
api.uuid = api.generateUUID(True)

loves = []


def getDirectMessage(api):
    api.USER_AGENT = 'Instagram 137.0.0.34.123 Android (18/4.3; 320dpi; 720x1280; Xiaomi; HM 1SW; armani; qcom; en_US)'
    api.getv2Inbox()
    for x in range(0, 9):
        if api.LastJson["inbox"]["threads"][x]['users'][0]['username'] == 'otherusername':
            try:
                message = api.LastJson["inbox"]["threads"][x]['items'][0]['text']
            except KeyError:
                message = 'Unsupported media format'

    return message

if (api.login()):
    starttime = time.time()
    numberOfApiLoads = 0
    lastMessage = ""
    while True:
        if lastMessage != getDirectMessage(api):
            print(getDirectMessage(api))
            lastMessage = getDirectMessage(api)

        if datetime.datetime.now().hour == 12:
            api.uuid = api.generateUUID(True)
            api.searchUsername('shelby.kelly')
            user_id = api.LastJson['user']['pk']
            api.direct_message("There have been " + str(len(loves)) + " love you's so far", user_id)

        if datetime.datetime.now().hour == 24:
            api.uuid = api.generateUUID(True)
            api.searchUsername('shelby.kelly')
            user_id = api.LastJson['user']['pk']
            api.direct_message("There have been " + str(len(loves)) + " love you's today", user_id)
            loves = []

        if getDirectMessage(api).lower().find('i love you') != -1:
            loves.append({'dayOfWeek':  datetime.datetime.today().weekday(), 'hour': datetime.datetime.now().hour})
            print(loves)


            api.uuid = api.generateUUID(True)
            api.searchUsername('otherusername')
            user_id = api.LastJson['user']['pk']
            response = random.randint(1, 3)

            if response == 1:
                api.direct_message("I <3 you too cutie", user_id)
            elif response == 2:
                api.direct_message("I <3 you too beautiful", user_id)
            elif response == 3:
                api.direct_message("I <3 you too gorgeous", user_id)




        time.sleep(2 - ((time.time() - starttime) % 2))

else:
    print("Can't login!")
