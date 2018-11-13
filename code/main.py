#!/usr/bin/python

import re

path = "/Users/JoshuaHowell/Desktop/Texas A&M/Year 2/Fall 2018/Natural Language Processing/Homework4/processed_docs/pos/cv000_29590.txt.out"
file  = open(path, 'r')

file_contents = file.read()

file.close()

# matchObj = re.match(r'[^_]*_JJ_[^_\s]*', file_contents, re.M|re.I)

# line = "films_NNS_B-NP adapted_VBN_B-VP from_IN_B-PP comic_JJ_B-NP books_NNS_I-NP have_VBP_B-VP    "
#line = "hi_hello comic_JJ_B-NP books_NNS_I-NP have_VBP_B-VP    "


matchObj = re.search(r'[\s]+[^_]*_JJ_[^_\s]*[\s]*[^_]*_(NN|NNS)_[^_\s]*[\s]*[^_]*_[^_]*_[^_\s]*', file_contents, re.M|re.I)

if matchObj:
     print "matchObj.group() : ", matchObj.group()


# line = "Cats are smarter than dogs"
#
# matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
#
# if matchObj:
#    print "matchObj.group() : ", matchObj.group()
#    print "matchObj.group(1) : ", matchObj.group(1)
#    print "matchObj.group(2) : ", matchObj.group(2)
# else:
#    print "No match!!"



#You have to use parenthesis (capture) in order to use the or operator
#However, you can use the (?: ) operator to ignore  the capture
# line = "films_NNS_B-NP adapted_VBN_B-VP from_IN_B-PP"
#
# matchObj = re.match(r'[^_]*_NNS_[^_\s]*[\s]*[^_]*_(?:VBN|QQ)_[^_\s]*[\s]*[^_]*_IN_[^_\s]*', line, re.M|re.I)
#
# if matchObj:
#      print "matchObj.group() : ", matchObj.group()
