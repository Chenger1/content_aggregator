from bs4 import BeautifulSoup

import requests
import json


res_data = {} 
'''
Contains information about web-sites to parse 
in format {'name':{
    'url':'http://something.com',
    'key':'key_to_parse',
    }
'''

with open('url_base.json', 'r') as base: #url saved in .json file
    url_base = json.loads(base.read())

def get_content(res_data=res_data, url_base=url_base):
    """Sends request to url which took from res_data"""
    for i in url_base:
        res_data[i] = {}
        response_data = requests.get(url_base[i]['url']).text
        soup = BeautifulSoup(response_data, 'html.parser')
        temp_data = soup.find_all(class_=url_base[i]['key'], limit=20)
        res_data[i] = [[j.attrs['href'], j.text] for j in temp_data]
    return res_data
"""
    m = [['habr',['url', 'text'], ['TechCrunch', ['url', 'text']]]
"""