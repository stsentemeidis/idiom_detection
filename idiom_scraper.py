# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 13:01:12 2019

@author: Dan
"""

import requests
from bs4 import BeautifulSoup

response = requests.get("https://7esl.com/english-idioms/")

soup = BeautifulSoup(response.text, "html.parser")

idioms = [strong_tag.get_text() for strong_tag in soup.select("td strong")]

print("Number of idioms: {}".format(len(idioms)))

with open("idioms.txt", "a") as f:
    for idiom in idioms:    
        f.write(idiom + "\n")


