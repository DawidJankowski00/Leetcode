class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        result = 0
        arr1.sort()
        arr2.sort()
        j = 0

        for v in arr1:
            while j < len(arr2) and arr2[j] < v - d:
                j += 1
            if j == len(arr2) or arr2[j] > v + d:
                result += 1
        return result