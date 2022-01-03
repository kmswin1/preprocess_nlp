import re, json
from kss import split_sentences
import sys
input = str(sys.argv[1])
output = str(sys.argv[2])

def clean_text(sentence):
    text = re.sub(r'[@%\\*=()/~#&\+á?\xc3\xa1\-\|\.\:\;\!\-\,\_\~\$\'\"]', '', sentence)  # remove punctuation
    text = re.sub(r'\d+', '', text)  # remove number
    text = text.lower()  # lower case
    text = re.sub(r'\s+', ' ', text) # remove extra space
    text = re.sub(r'\[[^)]*\]','',text)  # [~]
    text = re.sub(r'<[^>]+>','',text) #remove Html tags
    text = re.sub(r'\s+', ' ', text) #remove spaces
    text = re.sub(r"^\s+", '', text) #remove space from start
    text = re.sub(r'\s+$', '', text) #remove space from the end
    text = re.sub('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', '', text) # remove email
    return text


def preprocess():
    with open(input, 'r') as f:
        with open(output, 'w') as ff:
            for line in f:
                text = line.strip()
                sentences = split_sentences(text)
                for sentence in sentences:
                    text = clean_text(sentence)
                    ff.write(text + '\n')

preprocess()