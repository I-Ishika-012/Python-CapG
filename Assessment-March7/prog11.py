'''
Prog.11
Description
Consecutive Duplicate Word Detector
Problem Description
A text processing tool analyzes sentences to find consecutive duplicate words.

If the same word appears next to each other, ignoring case differences, it should be recorded.

Return a list of such duplicate words.

Input
A sentence string.

Output
List of duplicate consecutive words.
'''

class Solution:
    def find_duplicate_words(self, sentence):
        words = sentence.lower().split()
        duplicates = []
        for i in range(len(words)-1):
            if words[i]==words[i+1]:
                duplicates.append(words[i])
       
        return duplicates