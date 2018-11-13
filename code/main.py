#!/usr/bin/python

import re

path = "/Users/JoshuaHowell/Desktop/Texas A&M/Year 2/Fall 2018/Natural Language Processing/Homework4/processed_docs/pos/cv000_29590.txt.out"
file  = open(path, 'r')

file_contents = file.read()

file.close()



#matches = re.findall(r'[\s]+[^_]*_JJ_[^_\s]*[\s]*[^_]*_(?:NN|NNS)_[^_\s]*[\s]*[^_]*_[^_]*_[^_\s]*', file_contents, re.M|re.I)


matches = re.findall(r'[\s]+[^_]*_(?:RB|RBR|RBS)_[^_\s]*[\s]*[^_]*_JJ_[^_\s]*[\s]*[^_]*_[^(?:NN|NNS)]*_[^_\s]*', file_contents, re.M|re.I)



for match in matches:
    print match
