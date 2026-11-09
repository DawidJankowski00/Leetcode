import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.isPrefixOfWord("i love eating burger", "burg"))
    print(time.time() - start)

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split()
        m = len(searchWord)
        for i, w in enumerate(sentence):
            if w[0:m] == searchWord:
                return i + 1
        return -1
        

if __name__ == '__main__':
    sys.exit(main())