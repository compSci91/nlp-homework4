#!/usr/bin/python

from phrase_retrieval import PhraseExtractor
from semantic_orientation import SemanticOrientationCalculator

class CrossValidator:
    def __init__(self, list_of_positive_file_paths, list_of_negative_file_paths):
        self.list_of_positive_file_paths = list_of_positive_file_paths
        self.list_of_negative_file_paths = list_of_negative_file_paths

    def performCrossValidation(self):
        #Everything is gotten in 100 file chunks
        positive_test_file_paths = self.list_of_positive_file_paths[0:100]
        positive_training_file_paths = self.list_of_positive_file_paths[100:1000]

        negative_test_file_paths = self.list_of_negative_file_paths[0:100]
        negative_training_file_paths = self.list_of_negative_file_paths[100:1000]

        semantic_orientation_calculator = SemanticOrientationCalculator(positive_training_file_paths, negative_training_file_paths)
        semantic_orientation_values = []

        positive_test_file_path = positive_test_file_paths[0]
        phrase_extractor = PhraseExtractor(positive_test_file_path)
        extracted_phrases = phrase_extractor.getTwoWordPhrases()

        for extracted_phrase in extracted_phrases:
            semantic_orientation_value = semantic_orientation_calculator.calculate_semantic_orientation(extracted_phrase)
            semantic_orientation_values.append(semantic_orientation_value)


        semantic_orientation_average = sum(semantic_orientation_values) / len(semantic_orientation_values)



        # for positive_test_file_path in positive_test_file_path:
        #     phrase_extractor = PhraseExtractor(positive_test_file_path)
        #     extracted_phrases = phrase_extractor.getTwoWordPhrases()


        # 1. Get first 100 positive files
        # 2. Get first 100 negative files
        # 3. For every positive file
            #3.1 Extract phrases
            #3.2 Get the Semantic Orientation of Every Phrase
            #3.3 Average the semantic Orientation of every Phrase
            #3.4 Classify the phrase
        #4. Do the same for every negative file
