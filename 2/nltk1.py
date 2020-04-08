# -*- coding: utf-8 -*-

from nltk.stem import PorterStemmer

from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.snowball import SnowballStemmer

if __name__ == '__main__':
   pst = PorterStemmer()
   lst = LancasterStemmer()
   print(lst.stem('eating'))
   print(pst.stem('shopping'))