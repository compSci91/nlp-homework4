#!/usr/bin/python
import re
import sys
from cross_validation import CrossValidator
from near import HitCalculator
from os import listdir
from os.path import isfile, join

positive_reviews_directory = sys.argv[1]
list_of_positive_files = [f for f in listdir(positive_reviews_directory) if isfile(join(positive_reviews_directory, f))]
list_of_positive_file_paths = [positive_reviews_directory + file_name for file_name in list_of_positive_files]

negative_reviews_directory = sys.argv[2]
list_of_negative_files = [f for f in listdir(negative_reviews_directory) if isfile(join(negative_reviews_directory, f))]
list_of_negative_file_paths = [negative_reviews_directory + file_name for file_name in list_of_negative_files]



cross_validator = CrossValidator(list_of_positive_file_paths, list_of_negative_file_paths)

cross_validator.performCrossValidation()
