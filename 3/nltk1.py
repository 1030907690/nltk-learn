# -*- coding: utf-8 -*-

import nltk
from nltk import word_tokenize
from nltk import ne_chunk

if __name__ == '__main__':
   # nltk.download('punkt')
   # nltk.download('averaged_perceptron_tagger')
   nltk.download('maxent_ne_chunker')
   sent = 'Mark is studying at stanford university in california'
   print(ne_chunk(nltk.pos_tag(word_tokenize(sent)),binary=False))