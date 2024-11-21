

from typing import List


def main():
    print(findLengthOfShortestSubarray([1,2,3]))

def findLengthOfShortestSubarray(arr: List[int]) -> int:
    result = 0
    for i in range(1, len(arr)):
        tabs = []
        j = 0
        while(j+i < len(arr)):
            tabs.append(arr[0:j-1]+arr[j:])
            j+=1
        print(tabs)
                


    return result
main()