from nltk import ngrams
import glob
import os
import nltk
from collections import defaultdict
from nltk.corpus import brown
from nltk import FreqDist

brownPath = "C:\\Users\\Adrian\\AppData\\Roaming\\nltk_data\\corpora\\brown"

files = glob.glob(brownPath + "/c[a-z][0-9][0-9]")

bigramfdist = FreqDist()

numNGrams = 0

for file in files:
    f = open(file, 'r')
    #(path, filename) = os.path.split(file)
    raw = f.read()
    tokens = nltk.word_tokenize(raw)
    bgs = ngrams(tokens, 2)
    #bigramfdist.update(bigrams)

print(bgs)