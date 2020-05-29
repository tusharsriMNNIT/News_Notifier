import os
from pygame import mixer
import time
import json
import notify2

def notify(msg, urgency='normal'):

        notify2.init('News_NOtifier')
        n = notify2.Notification('News_NOtifier', msg, icon='/home/coder/Desktop/News_Notifier/icon.png')
        n.timeout = 1
        n.set_urgency({
            'low': notify2.URGENCY_LOW,
            'normal': notify2.URGENCY_NORMAL,
            'critical': notify2.URGENCY_CRITICAL,
        }.get(urgency))
        n.show() 
        mixer.init()
        mixer.music.load('swiftly.mp3')
        mixer.music.play()
        time.sleep(12)

with open('/home/coder/Desktop/News_Notifier/Notifier/news.json') as f:
    data = json.load(f)

for item in data:
    print(item['tile'])
    notify(item['title'])