import re, string                                                       #regular expression 
import nltk                                                          #working with text
from nltk.tokenize import sent_tokenize                              #function for text -> sentence



nltk.download("punkt", quiet=True)

def clean(text: str)-> str:
    text = ''.join(char for char in text if char.isprintable())             #remove non printable characters
    text = re.sub(r'\s+', ' ',text)                                         #substitution pattern -> (pattern, replacement, text)                                               
    return text

#NLP - sent_tokenize -> list of individual sentences
def split_into_sentences(text: str) -> list[str]:
    return sent_tokenize(text)

def read_image():                                               #OCR related (future project)
    return 0