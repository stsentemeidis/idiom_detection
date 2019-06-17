import os.path
from datetime import datetime
import re

IDIOMS_FILE = "idioms.txt"

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

def clear_file(output_file):
    if os.path.exists(output_file):
        with open(output_file, "w") as f:
            f.write("")
            

#KNOWN BUG(?): Information loss - everything is lowercased

#KNOWN BUG: idiom in one context, not another.
# e.g.: "all the same, ..." (an idiom) vs "they are not all the same" (not an idiom) 
            
def write_tagged_sentences(sents, output_file, idioms_file=IDIOMS_FILE):
    print("Starting script execution: {}".format(datetime.now()))          
    
    for i in range(len(sents)):
        # enumerate breaks the NLTK code for some reason, so had to do it this way
        sent = sents[i]
        
        if i % 500 == 0:
            print("{}: Tagged {} of {} sentences..."
                  .format(datetime.now(),i, len(sents)))
        
        sent_text = " ".join(sent).lower()
        
        with open(idioms_file, "r") as f:
            for line in f.readlines():
                idiom = line.lower().strip()
                if has_idiom(sent_text, idiom):
                    sent_text = sent_text.replace(idiom, tag_idiom(idiom))
                
        with open(output_file, "a") as f:
            f.write(sent_text + "\n")
                    
    print("Finishing script execution: {}".format(datetime.now()))
    
    return True
    
    
def num_found_idioms(file):
    with open(file, "r") as f:
        count = 0
        for line in f.readlines():
            if "#BEGIN" in line:
                count += 1
    
    return count
    
