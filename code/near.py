#!/usr/bin/python

import re

path = "/Users/JoshuaHowell/Desktop/Texas A&M/Year 2/Fall 2018/Natural Language Processing/Homework4/processed_docs/pos/cv017_22464.txt.out"
file  = open(path, 'r')

file_contents = file.read()

file.close()

##STILL NEED TO DO THE REVERSE

def numberOfHitsPriorToExcellent(phrase_regex, file_contents):
    word_regex = '(?:\s[^_]*_[^_]*_[^_\s]*){1,6}?'
    excellent_regex = '(?:\sexcellent_[^_]*_[^_\s]*)'
    matches = re.findall(r''+phrase_regex + word_regex +  excellent_regex, file_contents, re.M|re.I)
    # for match in matches:
    #     print match
    return len(matches)

def numberOfHitsAfterExcellent(phrase_regex, file_contents):
        phrase_regex = '\s' + phrase_regex
        word_regex = '(?:\s[^_]*_[^_]*_[^_\s]*){1,6}?'
        excellent_regex = '(?:\sexcellent_[^_]*_[^_\s]*)'
        matches = re.findall(r''+excellent_regex + word_regex +  phrase_regex, file_contents, re.M|re.I)
        # for match in matches:
        #     print match
        return len(matches)


def numberOfHitsNearExcellent(phrase, file_contents):
    phrase = phrase.replace(' ', '\s')
    phrase_regex = '(?:' + phrase + ')'
    return numberOfHitsNearExcellent(phrase_regex, file_contents) + numberOfHitsAfterExcellent(phrase_regex, file_contents)


print numberOfHitsNearExcellent('memorable_JJ_I-NP score_NN_I-NP ,_,_B-O', file_contents)
# numberOfHitsAfterExcellent('(?:,_,_B-O)', file_contents)
# matches = re.findall(r''+ '(?:excellent_JJ_I-NP acting_NN_I-NP ,_,_B-O)', file_contents, re.M|re.I)
# for match in matches:
#     print match
