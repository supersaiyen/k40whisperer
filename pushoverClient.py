#!/usr/bin/env python
from pushover import Client
import json

def sendPush(messageToSend, title):
    with open('pushoverConfig.json') as f:
        data = json.load(f)
        for user in data["users"]:
            Client(user["key"], api_token=data["apiKey"]).send_message(messageToSend, title=title)