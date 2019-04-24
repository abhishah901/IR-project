# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 17:01:25 2019

@author: abhis
"""

# -- imports --

from xml.dom import minidom
import urllib
import requests
from nltk.tokenize.punkt import PunktSentenceTokenizer
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
import io
from nltk.tokenize import sent_tokenize
from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords
import numpy as np
import docx2txt
import sys
import matplotlib.pyplot as plt 
import networkx as nx
from nltk.tokenize.punkt import PunktSentenceTokenizer
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
import sys
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
import io
from nltk.tokenize import sent_tokenize
import urllib
from bs4 import BeautifulSoup
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser
import prepper
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.edmundson import EdmundsonSummarizer
import itertools
import os
import lsa.py
import prepper.py
import luhn.py
import edmund.py
import summarizer.py
import pointergenerator.py
import scisum.py