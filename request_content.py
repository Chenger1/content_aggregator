import requests
import json
from bs4 import BeautifulSoup

res_data = {} 
'''
Contains imformation about web-sites to parse 
in format {'name':{
    'url':'http://something.com',
    'key':'key_to_parse',
    }
'''

with open('url_base.json', 'r') as base: #url saved in .json file
    url_base = json.loads(base.read())

def get_content():
    """Send request to url which taked from res_data"""
    for i in url_base:
        response_data = requests.get(url_base[i]['url']).text
        soup = BeautifulSoup(response_data, 'html.parser')
        data = soup.find_all(class_=url_base[i]['key'], limit=20)
        res_data[i] = data  
    return res_data


'''These functions would be helpful in the future'''
# def make_request():
#     data = requests.get(url_base['techcrunch']['url'])
#     return data.text

# def make_parse(data):
#     soup = BeautifulSoup(data, 'html.parser')
#     data = soup.find_all(class_='post-block')
#     return data