import sys
from typing import List
def main():
    sol = Solution()
    print(sol.merge([1,2,3,0,0,0], 3, [2,5,6], 3))

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m+n -1
        while i > -1:
            if m <= 0:
                nums1[i] = nums2[n-1]
                n -=1
                i -= 1
                continue
            elif n <= 0:
                nums1[i] = nums1[m-1]
                m-=1
                i -= 1
                continue
            if nums1[m-1] <= nums2[n-1]:
                nums1[i] = nums2[n-1]
                n -= 1
            else:
                nums1[i] = nums1[m-1]
                m -= 1
            i -= 1
        

if __name__ == '__main__':
    sys.exit(main())