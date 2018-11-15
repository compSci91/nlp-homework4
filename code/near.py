#!/usr/bin/python

import re

# path = "/Users/JoshuaHowell/Desktop/Texas A&M/Year 2/Fall 2018/Natural Language Processing/Homework4/processed_docs/pos/cv017_22464.txt.out"
# path = "/Users/JoshuaHowell/Desktop/Texas A&M/Year 2/Fall 2018/Natural Language Processing/Homework4/processed_docs/neg/cv013_10494.txt.out"
# file  = open(path, 'r')
#
# file_contents = file.read()
#
# file.close()

##STILL NEED TO DO THE REVERSE

class HitCalculator:
    def __init__(self, list_of_file_paths):
        self.file_contents = ''
        for file_path in list_of_file_paths:
            file = open(file_path, 'r')
            self.file_contents = self.file_contents + file.read() + ' '
            file.close()

    def numberOfHitsPrior(phrase_regex, nearby_phrase, file_contents):
        word_regex = '(?:\s[^_]*_[^_]*_[^_\s]*){1,6}?'
        excellent_regex = '(?:\s'+ nearby_phrase + '_[^_]*_[^_\s]*)'
        matches = re.findall(r''+phrase_regex + word_regex +  excellent_regex, file_contents, re.M|re.I)
        for match in matches:
            print match
        return len(matches)

    def numberOfHitsAfter(phrase_regex, nearby_phrase, file_contents):
            phrase_regex = '\s' + phrase_regex
            word_regex = '(?:\s[^_]*_[^_]*_[^_\s]*){1,6}?'
            excellent_regex = '(?:\s'+ nearby_phrase + '_[^_]*_[^_\s]*)'
            matches = re.findall(r''+excellent_regex + word_regex +  phrase_regex, file_contents, re.M|re.I)
            for match in matches:
                print match
            return len(matches)

    def numberOfHitsNear(phrase, nearby_phrase):
        phrase = phrase.replace(' ', '\s')
        phrase_regex = '(?:' + phrase + ')'
        return numberOfHitsPrior(phrase_regex, nearby_phrase, self.file_contents) + numberOfHitsAfter(phrase_regex, nearby_phrase, self.file_contents)

    def numberOfHits(self, nearby_phrase):
        nearby_phrase_regex = '(?:\s'+ nearby_phrase + '_[^_]*_[^_\s]*)'
        matches = re.findall(r''+nearby_phrase_regex, self.file_contents, re.M|re.I)
        for match in matches:
            print match
        return len(matches)


# print numberOfHitsNear('shao_JJ_B-NP khan_NN_I-NP was_VBD_B-VP', 'poor', file_contents)
