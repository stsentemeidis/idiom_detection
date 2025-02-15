import os.path
from datetime import datetime
import re
from nltk import pos_tag

IDIOMS_FILE = "./data/idioms.txt"

def text_has_idiom(text, idiom):
    text = text.lower()
    idiom_start = text.find(idiom)
    
    if idiom_start == -1:
        return False
    else:

        try:
            alpha_before = idiom_start != 0 and re.match("[a-zA-Z]", text[idiom_start-1])
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

def retain_case(word, word_lower):
    if "#" in word_lower:
        tag = word_lower.split("#")[1]
        word = word + "#" + tag
    return word

def replace_with_tag(text, idiom):
    text_lower = text.lower()
    
    if text_has_idiom(text_lower, idiom):
        text_lower = text_lower.replace(idiom, tag_idiom(idiom))

        text_as_list = [retain_case(word, word_lower) \
                        for word, word_lower in zip(text.split(),
                                                    text_lower.split())
                        ]
    
        text = " ".join(text_as_list)
    
    return text

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
        
        sent_text = " ".join(sent)
        
        with open(idioms_file, "r") as f:
            for line in f:
                idiom = line.lower().strip()
                sent_text = replace_with_tag(sent_text, idiom)
                
        with open(output_file, "a") as f:
            f.write(sent_text + "\n")
                    
    print("Finishing script execution: {}".format(datetime.now()))
    
    return True
    
    
def num_found_idioms(file):
    with open(file, "r") as f:
        count = 0
        for line in f:
            if "#BEGIN" in line:
                count += 1
    
    return count


def word_to_tags(word):
    if "#" in word:
        word, tag = word.split("#")
    else:
        tag = "OUT"

    ps = pos_tag([word])[0][1]

    return word, ps, tag





    
    
