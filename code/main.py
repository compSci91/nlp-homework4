#!/usr/bin/python
import re
from cross_validation import CrossValidator
from near import HitCalculator
from os import listdir
from os.path import isfile, join

positive_reviews_directory = "/Users/JoshuaHowell/Desktop/Texas A&M/Year 2/Fall 2018/Natural Language Processing/Homework4/processed_docs/pos/"
list_of_positive_files = [f for f in listdir(positive_reviews_directory) if isfile(join(positive_reviews_directory, f))]
list_of_positive_file_paths = ['../processed_docs/pos/' + file_name for file_name in list_of_positive_files]

negative_reviews_directory = "/Users/JoshuaHowell/Desktop/Texas A&M/Year 2/Fall 2018/Natural Language Processing/Homework4/processed_docs/neg/"
list_of_negative_files = [f for f in listdir(negative_reviews_directory) if isfile(join(negative_reviews_directory, f))]
list_of_negative_file_paths = ['../processed_docs/neg/' + file_name for file_name in list_of_negative_files]


pattern = re.compile('worst')
for m in pattern.finditer("This is the worst project ever"):
    print m.span()





# cross_validator = CrossValidator(list_of_positive_file_paths, list_of_negative_file_paths)
#
# cross_validator.performCrossValidation()
