import re

class PhraseExtractor:
    def __init__(self, path):
        path = "/Users/JoshuaHowell/Desktop/Texas A&M/Year 2/Fall 2018/Natural Language Processing/Homework4/processed_docs/pos/cv007_4968.txt.out"
        file  = open(path, 'r')

        file_contents = file.read()

        file.close()

        list1 = re.findall(r'[\s]+[^_]*_JJ_[^_\s]*[\s]*[^_]*_(?:NN|NNS)_[^_\s]*[\s]*[^_]*_[^_]*_[^_\s]*', file_contents, re.M|re.I)
        list2 = re.findall(r'[\s]+[^_]*_(?:RB|RBR|RBS)_[^_\s]*[\s]*[^_]*_JJ_[^_\s]*[\s]*[^_]*_[^(?:NN|NNS)]*_[^_\s]*', file_contents, re.M|re.I)
        list3 = re.findall(r'[\s]+[^_]*_JJ_[^_\s]*[\s]*[^_]*_JJ_[^_\s]*[\s]*[^_]*_[^_]*_[^_\s]*', file_contents, re.M|re.I)
        list4 = re.findall(r'[\s]+[^_]*_(?:NN|NNS)_[^_\s]*[\s]*[^_]*_JJ_[^_\s]*[\s]*[^_]*_[^(?:NN|NNS)]*_[^_\s]*', file_contents, re.M|re.I)
        list5 = re.findall(r'[\s]+[^_]*_(?:RB|RBR|RBS)_[^_\s]*[\s]*[^_]*_(?:VB|VBD|VBN|VBG)_[^_\s]*[\s]*[^_]*_[^_]*_[^_\s]*', file_contents, re.M|re.I)

        phrases = list1 + list2 + list3 + list4 + list5

        self.two_word_phrases = [phrase.rsplit(' ', 1)[0].strip() for phrase in phrases]

    def getTwoWordPhrases(self):
        return self.two_word_phrases
