

from typing import List


def main():
    print(twoSum([3,2,4], 6))

def twoSum(nums: List[int], target: int) -> List[int]:
    result = []
    for i in range(0, len(nums)):
        for j in range(0, len(nums)):
            if i == j:
                continue
            if nums[i] + nums[j] == target:
                result.append(i)
                result.append(j)
                break
        if len(result) > 0:
            break
    return result
main()