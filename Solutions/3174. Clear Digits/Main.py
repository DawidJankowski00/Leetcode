from collections import defaultdict
import sys
import time

def main():
    sol = Solution()
    start = time.time()
    print(sol.clearDigits("cb34"))
    print(time.time() - start)



class Solution:
    def clearDigits(self, s: str) -> str:
        result = []
        for c in s:
            if c.isalpha():
                result.append(c)
            else:
                result.pop()
        return "".join(result)


        

if __name__ == '__main__':
    sys.exit(main())