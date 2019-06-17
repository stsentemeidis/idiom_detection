# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 13:01:12 2019

@author: Dan
"""

import requests
from bs4 import BeautifulSoup
import os.path

OUTPUT_FILE = "idioms.txt"

response = requests.get("https://7esl.com/english-idioms/")

soup = BeautifulSoup(response.text, "html.parser")

idioms = [strong_tag.get_text() for strong_tag in soup.select("td strong")]

print("Number of idioms: {}".format(len(idioms)))

# Clear contents if the file exists
if os.path.exists(OUTPUT_FILE):
    with open(OUTPUT_FILE, "w") as f:
        f.write("")

with open("idioms.txt", "a") as f:
    for idiom in idioms:    
        f.write(idiom + "\n")


