import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.intToRoman(3749))
    print(time.time() - start)

class Solution:
    def intToRoman(self, num: int) -> str:
        values = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }
        result = ""
        for i in range(4, -1, -1):
            while num >= 10**i:
                result += values[10**i]
                num -= 10**i
        return result.replace("CCCCCCCCC", "CM").replace("CCCCC", "D").replace("CCCC", "CD").replace("XXXXXXXXX", "XC").replace("XXXXX", "L").replace("XXXX", "XL").replace("IIIIIIIII", "IX").replace("IIIII", "V").replace("IIII", "IV")

        

if __name__ == '__main__':
    sys.exit(main())