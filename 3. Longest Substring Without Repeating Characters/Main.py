import sys
from typing import List
def main():
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        maxValue = 1
        currentSubstring = 0
        mapHas = {}
        l = 0
        r = 0
        while len(s) > r:
            if s[r] in mapHas:
                mapHas[s[r]] += 1
            else:
                mapHas[s[r]] = 1
            currentSubstring += 1
            while mapHas[s[r]] > 1:
                mapHas[s[l]] -= 1
                l += 1
                currentSubstring -= 1
                
            if currentSubstring > maxValue:
                maxValue = currentSubstring
            r += 1

        return maxValue
        

if __name__ == '__main__':
    sys.exit(main())