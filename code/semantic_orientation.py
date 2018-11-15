#!/usr/bin/python

from os import listdir
from os.path import isfile, join
from near import HitsCalculator
import math

class SemanticOrientationCalculator:
    def __init__(self, list_of_positive_file_paths, list_of_negative_file_paths):
        self.list_of_files = [val for pair in zip(list_of_positive_files, list_of_negative_files) for val in pair]

    def calculate_semantic_orientation(self, phrase):
        hitsCalculator = HitsCalculator(self.list_of_files)
        numberOfHitsExcellent = hitsCalculator.numberOfHitsNear()
        phrase_ration = (numberOfHitsNearExcellent * numberOfHitsPoor) / (numberOfHitsNearPoor * numberOfHitsExcellent)
        return math.log(phrase_ratio, 2)
