# -*- coding: utf-8 -*-

import pandas as pd
import requests
import re
import json
import unicodedata
# from utils import clear_file
from bs4 import BeautifulSoup

OUTPUT_FILE = "idioms.txt"

response = requests.get("https://7esl.com/english-idioms/")
soup = BeautifulSoup(response.text, "lxml")
r_text = soup.find_all('li')
# .get_text(strip=True)

# r_text = response.text.encode('utf-8')

idioms = []
sentences = []
for l in r_text:
  if re.search('<li><em>',str(l)):
#     print(l)
    keyword = re.findall('<strong>(.*?)<\/strong>',str(l))
    if len(keyword):
      keyword = re.sub('<em>|<\/em>|\(','',keyword[0])
    else:
      keyword = re.findall('<strong style=\"font-style: inherit;\">(.*?)</strong>', str(l))
      keyword = re.sub('<em>|<\/em>|\(','',keyword[0])
      
    sentence = re.sub('(<\w+>)|(<\/\w+>)|(\(.*?\))|(<strong style=\"font-style: inherit;\">)','',str(l))
    sentence = re.sub('(\s+)',' ',sentence)
    idioms.append(keyword)
    sentences.append(sentence)
    print(keyword)
    print(sentence)
    print("===============================")
    
example_df = pd.DataFrame({'idiom':idioms, 'sentence':sentences})
example_df['idiom'] = example_df['idiom'].map(lambda x: re.sub('\(','',str(x)))
example_df.to_csv('/data/idiom_example.csv')