# NLP Brown Corpus Shenanigans

Python scripts that play around with the NLTK Brown Corpus. Some functionalities include finding all bigrams and trigrams, frequency of a part-of-speech (POS) given another POS, etc.

## Setup 
Fork the scripts and download them locally. **Must** change the "brownPath" in the brown.py and brown-num-n-grams.py scripts to be able to run correctly.

### Dependencies

* Python "collections" library - comes with Python 2 & 3 installations
* NLTK library (brown-num-n-grams.py, brown-num-sentences.py)
* PyDictionary library (brown-num-sentences.py)

### Installation

* Mac OS X
* Ubuntu
* Windows
* Python
* NLTK library

```python
sudo pip install -U nltk
```

* PyDictionary library

```python
pip install PyDictionary
```

## Usage

Mostly just wanted to play around with the Brown corpus. Functionalities of all three scripts include:
* Total frequency of a category in the corpus
* Total frequency of a POS in the corpus
* Frequency of a POS given a POS
* Total frequency of a word in the corpus
* Frequency of a word given a POS
* Frequency of a word given a word (bigram)
* Frequency of a word given a word given a word (trigram)
* Total number of sentences in the corpus

## Demo (sample image)

Image displaying the probability of a part-of-speech (first column) given a part-of-speech (second column).

![image](https://user-images.githubusercontent.com/14877762/58758083-05ad9400-84cb-11e9-985c-9128b1965783.png)


## Errors and bugs

If something is not behaving intuitively, it is a bug and should be reported.
Report it here by creating an issue: https://github.com/adrianmoo2/nlp-brown-corpus-shenanigans/issues/new

Help us fix the problem as quickly as possible by following [Mozilla's guidelines for reporting bugs.](https://developer.mozilla.org/en-US/docs/Mozilla/QA/Bug_writing_guidelines#General_Outline_of_a_Bug_Report)

## Patches and pull requests

Your patches are welcome. Here's our suggested workflow:
 
* Fork the project.
* Make your feature addition or bug fix.
* Send us a pull request with a description of your work. Bonus points for topic branches!
