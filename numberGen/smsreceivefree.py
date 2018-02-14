import os
import json
import time
import random
import requests
from lxml import html

class util:
    def getCC(self,country):
        filepath = os.path.join(os.path.dirname(__file__),'countryCode.json')
        with open(filepath) as jsonFile:
            data = json.load(jsonFile)
        return data[country]

class generator:
    def __init__(self,):
        self.url = 'https://smsreceivefree.com/'

    def getNumber(self,country):
        url = "{0}country/{1}".format(self.url, country)
        r = requests.get(url)
        tree = html.fromstring(r.content)
        numbers = tree.xpath('//*[@class="row"]/a/text()')
        paths = tree.xpath('//*[@class="row"]/a/@href')
        selected = random.randint(0,len(paths))
        number = numbers[selected].split(" ")[0]
        self.path = paths[selected]
        return number, country

    def checkSMS(self,pattern):
        url = "{0}{1}/".format(self.url,self.path)
        r = requests.get(url)
        tree = html.fromstring(r.content)
        sender = tree.xpath('//*[@class="msgTable"]/tbody/tr/td[1]/text()')
        message = tree.xpath('//*[@class="msgTable"]/tbody/tr/td[3]/text()')
        for x in range(5):
            if pattern in message[x]:
                return message[x]
                break
