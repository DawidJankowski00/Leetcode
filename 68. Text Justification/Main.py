import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.fullJustify(["What","must","be","acknowledgment","shall","be"], 16))
    print(time.time() - start)

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        tmp = [words[0]]
        i = len(words[0])
        for k, w in enumerate(words):
            if k == 0:
                continue
            if len(w) + i + 1 > maxWidth:
                s = maxWidth - i
                j = 0
                while s != 0:
                    tmp[j] += " "
                    j += 1
                    if j >= len(tmp)-1:
                        j = 0
                    s -= 1
                result.append(" ".join(tmp))
                i = len(w)
                tmp = [w]
            else:
                tmp.append(w)
                i += 1 + len(w)
        if len(tmp) > 0:
            tmp = " ".join(tmp)
            s = maxWidth - len(tmp)
            tmp += " " * s
            result.append(tmp)
        return result
        

if __name__ == '__main__':
    sys.exit(main())