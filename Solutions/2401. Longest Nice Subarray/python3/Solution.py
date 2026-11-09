import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.longestNiceSubarray([84139415,693324769,614626365,497710833,615598711,264,65552,50331652,1,1048576,16384,544,270532608,151813349,221976871,678178917,845710321,751376227,331656525,739558112,267703680]))
    print(time.time() - start)

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        result = 1
        curr = nums[0]
        l = 0
        r = 1
        n = len(nums)
        while r < n:
            if curr & nums[r] == 0:
                curr += nums[r]
                r += 1
            else:
                result = max(r-l, result)
                curr -= nums[l]
                l += 1 
        result = max(result, r-l)
        return result
        

if __name__ == '__main__':
    sys.exit(main())