#!/usr/bin/python

from phrase_retrieval import PhraseExtractor
from near import HitCalculator
from os import listdir
from os.path import isfile, join

positive_reviews_directory = "/Users/JoshuaHowell/Desktop/Texas A&M/Year 2/Fall 2018/Natural Language Processing/Homework4/processed_docs/pos/"
list_of_positive_files = [f for f in listdir(positive_reviews_directory) if isfile(join(positive_reviews_directory, f))]
list_of_file_paths = ['../processed_docs/pos/' + file_name for file_name in list_of_positive_files]

hitsCalculator = HitCalculator(list_of_file_paths)
print hitsCalculator.numberOfHits('excellent')
