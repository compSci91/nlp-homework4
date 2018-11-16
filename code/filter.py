#!/usr/bin/python
import re

class Filter:
    def get_excellent_training_files(self, unfiltered_training_files):
        filtered_training_files = []

        for file_path in unfiltered_training_files:
            file = open(file_path, 'r')
            file_contents = file.read()
            file.close()

            if self.numberOfHits('excellent', file_contents) >= 1:
                print "Found a file with excellent!"
                filtered_training_files.append(file_path)

        return filtered_training_files

    def get_poor_training_files(self, unfiltered_training_files):
        filtered_training_files = []

        for file_path in unfiltered_training_files:
            file = open(file_path, 'r')
            file_contents = file.read()
            file.close()

            if self.numberOfHits('poor', file_contents) >= 1:
                print "Found a file with poor!"
                filtered_training_files.append(file_path)

        return filtered_training_files

    def numberOfHits(self, nearby_phrase, file_contents):
        nearby_phrase_regex = '(?:\s'+ nearby_phrase + '_[^_]*_[^_\s]*)'
        matches = re.findall(r''+nearby_phrase_regex, file_contents, re.M|re.I)
        return len(matches)
