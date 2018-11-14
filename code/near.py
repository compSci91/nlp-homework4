#!/usr/bin/python

import re

path = "/Users/JoshuaHowell/Desktop/Texas A&M/Year 2/Fall 2018/Natural Language Processing/Homework4/processed_docs/pos/cv013_10159.txt.out"
file  = open(path, 'r')

file_contents = file.read()

file.close()

# file_contents = file_contents.replace('\n', ' ')


#matches = re.findall(r'[\s]+[^_]*_JJ_[^_\s]*[\s]*[^_]*_(?:NN|NNS)_[^_\s]*[\s]*[^_]*_[^_]*_[^_\s]*', file_contents, re.M|re.I)

# phrase_regex = '(?:anthony_JJ_B-NP hopkins_NNS_I-NP turn_VBP_B-VP)'
phrase_regex = '(?:story_NN_I-NP\s._._B-O\sdjimon_JJ_B-NP)'
#
word_regex = '(?:\s[^_]*_[^_]*_[^_\s]*){1,6}?'
excellent_regex = '(?:\sexcellent_[^_]*_[^_\s]*)'
matches = re.findall(r''+phrase_regex + word_regex +  excellent_regex, file_contents, re.M|re.I)

for match in matches:
    print match


# test_string = ' turn_VBP_B-VP in_IN_B-PP '
# matches = re.findall(r''+word_regex, test_string, re.M|re.I)
#
# for match in matches:
#     print match
