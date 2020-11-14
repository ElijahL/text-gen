from collections import Counter
import re

# Reading texts
with open('/Users/ilia/Documents/TextGen/train/zavodnoy_apelsin.txt', 'r') as file:
    zavodnoy_apelsin = file.read()
with open('/Users/ilia/Documents/TextGen/train/po_kom_zvonit_kolokol.txt', 'r') as file:
    po_kom_zvonit_kolokol = file.read()

# Prepare corpus for training
zavodnoy_apelsin = zavodnoy_apelsin.replace('.', ' END')
po_kom_zvonit_kolokol = po_kom_zvonit_kolokol.replace('.', ' END') 

zavodnoy_apelsin_words = zavodnoy_apelsin.split()
po_kom_zvonit_kolokol_words = po_kom_zvonit_kolokol.split()

corpus = po_kom_zvonit_kolokol_words + zavodnoy_apelsin_words

def distribution(corpus):
    # Frequency of occurancy of words in corpus
    #
    # Creating dictionary where 
    # KEY is a word and VALUE is this word's frequncy of occurance
    dist = dict()
    for token in corpus:
        if token in dist:
            dist[token] += 1
        else:
            dist[token] = 1
    return dist


# Windows of words
windows = []
length = len(corpus)
for i in range(0, length - 1):
    windows.append((corpus[i], corpus[i + 1]))
    # connections.append([(corpus[j]) for j in range(i, i+1)])
windows.append((corpus[i], None))
    
def make_higher_order_windows(corpus):
    windows = []
    length = len(corpus)
    for i in range(0, length - 2):
        windows.append((corpus[i], corpus[i + 1], corpus[i + 2]))
    windows.append((corpus[i], corpus[i + 1], None))
    return windows

higher_order_windows = make_higher_order_windows(corpus)

