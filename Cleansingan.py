import re
import pandas as pd
import nltk
from nltk.corpus import stopwords
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory, StopWordRemover, ArrayDictionary


data_slang = pd.read_csv("D:/Binar/Data challenge/Data/new_kamusalay.csv", encoding = 'latin-1', header = None)
aslang = data_slang[0].values.tolist()
bslang = data_slang[1].values.tolist()

def pisah(text):
    text = str(text)
    return text.split()

def lowering(text):
    text = str(text)
    return text.lower()


def textbersih(text):
    text = re.sub('user',' ', str(text))
    text = re.sub('[^a-zA-Z0-9]',' ', str(text))
    text = re.sub('rt',' ', str(text))
    text = re.sub('x[a-z0-9]{1,2}',' ', str(text))
    text = re.sub('\s+',' ', str(text))
    text = re.sub('url',' ', str(text))
    return text


def slangan(text):
    dslang = dict(zip(aslang, bslang))
    katabaku = []
    for wrd in text:
        katabaku.append(dslang.get(wrd, wrd))
    return ' '.join(katabaku)


def bersihan(text):
    stop_words = stopwords.words("indonesian")
    stop_factory = StopWordRemoverFactory().get_stop_words()
    kata = set(stop_words + stop_factory)
    filtered_sent=[]
    for w in text:
        if w not in kata:
            filtered_sent.append(w)
    return ' '.join(filtered_sent)
