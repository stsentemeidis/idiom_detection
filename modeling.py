INPUT = ["./data/tagged_sentences_brown.txt"]

from utils import word_to_tags
from datetime import datetime

def tag_line(line):
    line = line.strip()
    tuples = [word_to_tags(w) for w in line.split(" ")]
    return tuples



print("{}: Reading tagged sentences...".format(datetime.now()))
for fname in INPUT:
    tagged_sentences = []
    with open(fname, "r") as f:     
        ts = [tag_line(line) for line in f]
        print("{}: tagged sentences from {}..."
              .format(datetime.now(), fname))
        
        tagged_sentences.extend(ts)
        print("{}: Added them to rest of sentences..."
              .format(datetime.now()))

print("{}: Finished!".format(datetime.now()))
            

def sent_has_idiom(sent):
    for _, _, itag in sent:
        if itag == "BEGIN":
            return True
    
    return False

with_idioms = [sent for sent in tagged_sentences if sent_has_idiom(sent)]
wo_idioms = [sent for sent in tagged_sentences if not sent_has_idiom(sent)]



    