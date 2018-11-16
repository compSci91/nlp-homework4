#!/usr/bin/python

from os import listdir
from os.path import isfile, join
from near import HitCalculator
import math

class SemanticOrientationCalculator:
    def __init__(self, list_of_positive_training_file_paths, list_of_negative_training_file_paths):
        self.training_files = [val for pair in zip(list_of_positive_training_file_paths, list_of_negative_training_file_paths) for val in pair]
        self.hitsCalculator = HitCalculator(self.training_files)
        self.phrase_dictionary = {}

    def calculate_semantic_orientation(self, extracted_phrases):
        semantic_orientation_values = []

        for phrase in extracted_phrases:
            if phrase in self.phrase_dictionary:
                semantic_orientation_values.append(self.phrase_dictionary[phrase])
            else:
                numberOfHitsNearExcellent = self.hitsCalculator.numberOfHitsNear(phrase, 'excellent') + 0.01
                numberOfHitsPoor = self.hitsCalculator.numberOfHitsPoor + 0.01

                numberOfHitsNearPoor = self.hitsCalculator.numberOfHitsNear(phrase, 'poor') + 0.01
                numberOfHitsExcellent = self.hitsCalculator.numberOfHitsExcellent + 0.01

                phrase_ratio = (numberOfHitsNearExcellent * numberOfHitsPoor) / (numberOfHitsNearPoor * numberOfHitsExcellent)
                linearized_phrase_ratio = math.log(phrase_ratio, 2)
                semantic_orientation_values.append(linearized_phrase_ratio)
                self.phrase_dictionary[phrase] = linearized_phrase_ratio



        if (len(semantic_orientation_values) == 0):
            return 0

        return sum(semantic_orientation_values) / len(semantic_orientation_values)
