# -*- coding: utf-8 -*-

import pandas as pd
import requests
import re
# from utils import clear_file

OUTPUT_FILE = "idioms.txt"

response = requests.get("https://7esl.com/english-idioms/")



r_text = response.text.encode()
r_content = re.findall('<h2><span class=\"ez-toc-section\" id=\"Idiom_Examples\">(.*?)<h2><span class=\"ez-toc-section\" id=\"Common_English_Idioms_Images\">',str(r_text))

li_list = re.findall('<li><em>(.*?)<\/em><\/li>', r_content[0])


idioms = []
sentences = []
for l in li_list:
  if 'Example' not in l:
    keyword = re.findall('<strong><em>(\w+.*?)<\/em></strong>', str(l))

    if len(keyword):
      keyword = re.sub('(<em>|<\/em>|<li>|</li>|<strong>|</strong>|\\\\|x\w\d)','',str(keyword[0]))
      sentence = re.sub('(<strong>|<strong style=\"font-style: inherit;\">)',' ',str(l))
      sentence = re.sub('(<em>|<\/em>|<li>|</li>|<strong>|<strong style=\"font-style: inherit;\">|</strong>|\\\\|x\w\d)','',sentence)

    else:
      l = re.sub('\\\\x\w\d','',str(l))
      keyword = re.findall('<strong style=\"font-style: inherit;\"><em>(\w+.*?)<\/em><\/strong>',str(l))
      if len(keyword):
        keyword = keyword[0]
        sentence = re.sub('(<em>|<\/em>|<li>|</li>|<strong>|<strong style=\"font-style: inherit;\">|</strong>|\\\\|x\w\d)','',str(l))

    sentence = re.sub('(\(.*?\))|(<\/ul>.*?)|(<\/p>.*?)|(<p.*?)|(<h3>.*?)','',sentence)

    idioms.append(keyword)
    sentences.append(sentence)

    

example_df = pd.DataFrame({'idiom':idioms, 'sentence':sentences})
example_df['idiom'] = example_df['idiom'].map(lambda x: re.sub('\(','',str(x)))
example_df.to_csv('idiom_example.csv')
