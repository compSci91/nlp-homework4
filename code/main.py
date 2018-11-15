#!/usr/bin/python

from phrase_retrieval import PhraseExtractor
from near import HitCalculator
from os import listdir
from os.path import isfile, join


# path = "/Users/JoshuaHowell/Desktop/Texas A&M/Year 2/Fall 2018/Natural Language Processing/Homework4/processed_docs/pos/"
#
# onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
#
# print onlyfiles


file_path = "/Users/JoshuaHowell/Desktop/Texas A&M/Year 2/Fall 2018/Natural Language Processing/Homework4/processed_docs/pos/cv013_10159.txt.out"
file_path1 = "/Users/JoshuaHowell/Desktop/Texas A&M/Year 2/Fall 2018/Natural Language Processing/Homework4/processed_docs/pos/cv017_22464.txt.out"

hitsCalculator = HitCalculator([file_path, file_path1])
print hitsCalculator.numberOfHits('excellent')


# list_of_positive_files = ["1", "2", "3"]
# list_of_negative_files = ["4", "5", "6"]
#
# interleaved_list = [val for pair in zip(list_of_positive_files, list_of_negative_files) for val in pair]
#
# for element in interleaved_list:
#     print element
