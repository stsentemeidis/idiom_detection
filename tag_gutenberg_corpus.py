from utils import write_tagged_sentences, clear_file, num_found_idioms
from nltk.corpus import gutenberg


OUTPUT_FILE = "./data/tagged_sentences_gutenberg.txt"

# Clear contents if the file exists
clear_file(OUTPUT_FILE)

## write to the file
success = write_tagged_sentences(gutenberg.sents(), OUTPUT_FILE)

if success:
    count = num_found_idioms(OUTPUT_FILE)
    print("number of idioms found (ish): {}".format(count))


            
