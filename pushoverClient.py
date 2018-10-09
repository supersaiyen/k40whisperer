#!/usr/bin/env python
from pushover import Client
import json
import os

def sendPush(messageToSend, title):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, 'pushoverConfig.json')) as f:
        data = json.load(f)
        for user in data["users"]:
            Client(user["key"], api_token=data["apiKey"]).send_message(messageToSend, title=title, sound="tugboat")