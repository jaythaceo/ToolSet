
import itertools
from operator import itemgetter
import networkx
import os
import nltk
"""
We are going to do the fucking impossible
with case law.

This text ranking program, will use special
machine learning algorithms.

"""
# Apply syntactic filters
def filter_for_tags(tagged, tags=['NN', 'JJ', 'NNP']):
  return [item for item in tagged if item[1] in tags]

def normalize(taggged):
  return [(item[0].replace('.', ''), item[1]) for item in taggged]

def unique_everseen():
  return

def lDistance():
  return


def buildGraph():
  return

def extractKeyPhrases():
  return

def extractSentances():
  return

def writeFiles():
  return