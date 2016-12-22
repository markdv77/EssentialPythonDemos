import requests


class Graph:
    def show(self):
        print('hello I am a super nice graph!')
        r = requests.get('http://google.com')
        print(r.text)
