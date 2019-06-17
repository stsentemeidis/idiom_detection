from nltk.corpus import brown
import os.path
from datetime import datetime
import re

INPUT_FILE = "idioms.txt"
OUTPUT_FILE = "tagged_sentences.txt"

# Fixing the problem of idiom appearing within other words
def has_idiom(text, idiom):
    idiom_start = text.find(idiom)
    
    if idiom_start != -1:
        try:
            alpha_before = re.match("[a-zA-Z]", text[idiom_start-1])
        except IndexError:
            alpha_before = False
        try:
            alpha_after = re.match("[a-zA-Z]", text[idiom_start + len(idiom)])
        except IndexError:
            alpha_after = False
            
        if alpha_before or alpha_after:
            return False
    
    return True
        
        

def tag_idiom(idiom):
    idiom_as_list = idiom.split(" ")
    
    for i,word in enumerate(idiom_as_list):
        if i == 0:
            idiom_as_list[i] = idiom_as_list[i] + "#BEGIN"
        else:
            idiom_as_list[i] = idiom_as_list[i] + "#IN"
            
    tagged = " ".join(idiom_as_list)
    
    return tagged

sents = brown.sents()

# Clear contents if the file exists
if os.path.exists(OUTPUT_FILE):
    with open(OUTPUT_FILE, "w") as f:
        f.write("")

print("Starting script execution: {}".format(datetime.now()))



#KNOWN BUG(?): Information loss - everything is lowercased

#KNOWN BUG: idiom in one context, not another.
# e.g.: "all the same, ..." (an idiom) vs "they are not all the same" (not an idiom) 



for i in range(len(sents)):
    # enumerate breaks the NLTK code for some reason, so had to do it this way
    sent = sents[i]
    
    if i % 500 == 0:
        print("{}: Tagged {} of {} sentences..."
              .format(datetime.now(),i, len(sents)))
    
    sent_text = " ".join(sent).lower()
    
    with open(INPUT_FILE, "r") as f:
        for line in f.readlines():
            idiom = line.lower().strip()
            if has_idiom(sent_text, idiom):
                sent_text = sent_text.replace(idiom, tag_idiom(idiom))
            
    with open(OUTPUT_FILE, "a") as f:
        f.write(sent_text + "\n")
                
print("Finishing script execution: {}".format(datetime.now()))
            
with open(OUTPUT_FILE, "r") as f:
    count = 0
    for line in f.readlines():
        if "#BEGIN" in line:
            count += 1

print("number of idioms found (ish): {}".format(count))
        
            
            
            
            
            
