from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        tmp = 0
        k = len(flowerbed)
        if k < 3:
            for v in flowerbed:
                if v == 1:
                    return n <= 0
            return n <= 1
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            tmp += 1
        for i in range(1, k - 1):
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                tmp += 1
        if flowerbed[k-2] == 0 and flowerbed[k-1] == 0:
            tmp += 1
        return tmp >= n
