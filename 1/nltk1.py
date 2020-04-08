# -*- coding: utf-8 -*-

import nltk
import requests
from  bs4 import BeautifulSoup

if __name__ == '__main__':
    html = requests.get('http://www.nltk.org/api/nltk.html#nltk.util.clean_html').text
#    clean = nltk.clean_html(html)
    clean = BeautifulSoup(html,"lxml").get_text()
    tokens = [tok for tok in clean.split()]
    print(tokens[:100])