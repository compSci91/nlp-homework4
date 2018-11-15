#!/usr/bin/python

from os import listdir
from os.path import isfile, join
from near import HitsCalculator
import math

class SemanticOrientationCalculator:
    def __init__(self, list_of_positive_test_file_paths, list_of_negative_test_file_paths):
        self.test_files = [val for pair in zip(list_of_positive_test_file_paths, list_of_negative_test_file_paths) for val in pair]

    def calculate_semantic_orientation(self, phrase):
        hitsCalculator = HitCalculator(self.test_files)

        numberOfHitsNearExcellent = hitsCalculator.numberOfHitsNear(phrase, 'excellent')
        numberOfHitsPoor = hitsCalculator.numberOfHits('poor')

        numberOfHitsNearPoor = hitsCalculator.numberOfHitsNear(phrase, 'poor')
        numberOfHitsExcellent = hitsCalculator.numberOfHits('excellent')

        phrase_ration = (numberOfHitsNearExcellent * numberOfHitsPoor) / (numberOfHitsNearPoor * numberOfHitsExcellent)
        return math.log(phrase_ratio, 2)
