import os, sys
import difflib
import time
import re
from PyDictionary import PyDictionary
from nltk.corpus import words
from nltk.corpus import brown

num_sentences = 0;

for fileid in brown.fileids():
    num_sentences += len(brown.sents(fileid))

print("num sentences in brown: " + str(num_sentences))
