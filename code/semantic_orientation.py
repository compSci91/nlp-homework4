#!/usr/bin/python

from os import listdir
from os.path import isfile, join
from near import HitCalculator
import math

class SemanticOrientationCalculator:
    def __init__(self, list_of_positive_training_file_paths, list_of_negative_training_file_paths):
        self.training_files = [val for pair in zip(list_of_positive_training_file_paths, list_of_negative_training_file_paths) for val in pair]

    def calculate_semantic_orientation(self, phrase):
        hitsCalculator = HitCalculator(self.training_files)

        numberOfHitsNearExcellent = hitsCalculator.numberOfHitsNear(phrase, 'excellent') + 0.01
        numberOfHitsPoor = hitsCalculator.getNumberOfHitsPoor('poor') + 0.01

        numberOfHitsNearPoor = hitsCalculator.numberOfHitsNear(phrase, 'poor') + 0.01
        numberOfHitsExcellent = hitsCalculator.getNumberOfHitsExcellent('excellent') + 0.01

        phrase_ratio = (numberOfHitsNearExcellent * numberOfHitsPoor) / (numberOfHitsNearPoor * numberOfHitsExcellent)
        return math.log(phrase_ratio, 2)
