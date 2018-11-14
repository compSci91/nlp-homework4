#!/usr/bin/python

# from os import listdir
# from os.path import isfile, join
#
# path = "/Users/JoshuaHowell/Desktop/Texas A&M/Year 2/Fall 2018/Natural Language Processing/Homework4/processed_docs/pos/"
#
# onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
#
# print onlyfiles

from phrase_retrieval import PhraseExtractor

path = "/Users/JoshuaHowell/Desktop/Texas A&M/Year 2/Fall 2018/Natural Language Processing/Homework4/processed_docs/pos/cv007_4968.txt.out"

PhraseExtractor(path)
