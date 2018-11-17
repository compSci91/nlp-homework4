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
    def __init__(self, list_of_positive_paths, list_of_negative_paths):
        self.positive_file_contents = ''
        self.negative_file_contents = ''

        for file_path in list_of_positive_paths:
            file = open(file_path, 'r')
            self.positive_file_contents = self.positive_file_contents + file.read() + ' '
            file.close()

        for file_path in list_of_negative_paths:
            file = open(file_path, 'r')
            self.negative_file_contents = self.negative_file_contents + file.read() + ' '
            file.close()

        self.numberOfHitsExcellent = self.numberOfHits('excellent')
        self.numberOfHitsPoor = self.numberOfHits('poor')

    def numberOfHitsNear(self, phrase, nearby_phrase):
        phrase = phrase.replace(' ', '\s')
        phrase_regex = '(?:' + phrase + ')'
        if nearby_phrase == 'excellent':
            # print "Looking for phrase near excellent"
            return self.numberOfHitsPrior(phrase_regex, nearby_phrase, self.positive_file_contents) + self.numberOfHitsAfter(phrase_regex, nearby_phrase, self.positive_file_contents)
        else:
            # print "looking for phrase near poor"
            return self.numberOfHitsPrior(phrase_regex, nearby_phrase, self.negative_file_contents) + self.numberOfHitsAfter(phrase_regex, nearby_phrase, self.negative_file_contents)


    def numberOfHitsPrior(self, phrase_regex, nearby_phrase, file_contents):
        word_regex = '(?:\s[^_]*_[^_]*_[^_\s]*){0,6}?'
        nearby_phrase_regex = '(?:\s'+ nearby_phrase + '_[^_]*_[^_\s]*)'
        matches = []
        try:
            matches = re.findall(r''+phrase_regex + word_regex +  nearby_phrase_regex, file_contents, re.M|re.I)
        except:
            ""

        return len(matches)

    def numberOfHitsAfter(self, phrase_regex, nearby_phrase, file_contents):
            phrase_regex = '\s' + phrase_regex
            word_regex = '(?:\s[^_]*_[^_]*_[^_\s]*){0,6}?'
            nearby_phrase_regex = '(?:\s'+ nearby_phrase + '_[^_]*_[^_\s]*)'
            matches = []
            try:
                matches = re.findall(r''+nearby_phrase_regex + word_regex +  phrase_regex, file_contents, re.M|re.I)
            except:
                ""

            return len(matches)

    def numberOfHits(self, nearby_phrase):
        file_contents = self.positive_file_contents + self.negative_file_contents
        nearby_phrase_regex = '(?:\s'+ nearby_phrase + '_[^_]*_[^_\s]*)'
        matches = re.findall(r''+nearby_phrase_regex, file_contents, re.M|re.I)
        return len(matches)




# print numberOfHitsNear('shao_JJ_B-NP khan_NN_I-NP was_VBD_B-VP', 'poor', file_contents)
