#!/usr/bin/python

from phrase_retrieval import PhraseExtractor
from semantic_orientation import SemanticOrientationCalculator

class CrossValidator:
    def __init__(self, list_of_positive_file_paths, list_of_negative_file_paths):
        self.list_of_positive_file_paths = list_of_positive_file_paths
        self.list_of_negative_file_paths = list_of_negative_file_paths

    def performCrossValidation(self):
        accuracies = []

        for fold_number in range(1, 10):
            positive_test_file_paths = self.list_of_positive_file_paths[fold_number*100:fold_number*100+100]
            positive_training_file_paths = self.list_of_positive_file_paths[0:fold_number*100] + self.list_of_positive_file_paths[fold_number*100+100:1000]

            negative_test_file_paths = self.list_of_negative_file_paths[fold_number*100:fold_number*100+100]
            negative_training_file_paths = self.list_of_negative_file_paths[0:fold_number*100] + self.list_of_negative_file_paths[fold_number*100+100:1000]

            semantic_orientation_calculator = SemanticOrientationCalculator(positive_training_file_paths, negative_training_file_paths)

            number_of_correct_classifications = 0;

            positive_file_number = 0
            for positive_test_file_path in positive_test_file_paths:
                print "Working on positive file: " + str(positive_file_number)
                positive_file_number+=1
                phrase_extractor = PhraseExtractor(positive_test_file_path)
                extracted_phrases = phrase_extractor.getTwoWordPhrases()
                semantic_orientation_average = semantic_orientation_calculator.calculate_semantic_orientation(extracted_phrases)
                print "Orientation is: " + str(semantic_orientation_average)
                if semantic_orientation_average > 0:
                    number_of_correct_classifications+=1

            negative_file_number = 0
            for negative_test_file_path in negative_test_file_paths:
                print "Working on negative file: " + str(negative_file_number)
                phrase_extractor = PhraseExtractor(negative_test_file_path)
                extracted_phrases = phrase_extractor.getTwoWordPhrases()
                semantic_orientation_average = semantic_orientation_calculator.calculate_semantic_orientation(extracted_phrases)
                print "Orientation is: " + str(semantic_orientation_average)
                if semantic_orientation_average < 0:
                    number_of_correct_classifications+=1

                negative_file_number+=1

            accuracy = number_of_correct_classifications/200.0
            accuracies.append(accuracy)
            print "[INFO] Fold " + str(fold_number) + " Accuracy: " + str(accuracy) + '\n'

        average_accuracy = sum(accuracies) / len(accuracies)
        print "[INFO] Accuracy: " + str(average_accuracy)
