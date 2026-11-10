from typing import List

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split()
        m = len(searchWord)
        for i, w in enumerate(sentence):
            if w[0:m] == searchWord:
                return i + 1
        return -1
