import sys
from typing import List
def main():
    sol = Solution()
    print(sol.decrypt([2,4,9,3], -2))

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        result = []
        if k == 0:
            for i in range(0, len(code)):
                result.append(0)
        elif k > 0:
            for i in range(0, len(code)):
                tmp = 0
                c = 0
                for j in range(1, k+1):
                    if i+j >= len(code):
                        tmp += code[c]
                        c += 1
                    else:
                        tmp += code[i+j]
                result.append(tmp)
        else:
            for i in range(0, len(code)):
                tmp = 0
                for j in range(1, -k+1):
                    tmp += code[i-j]
                result.append(tmp)
        return result
            


        

if __name__ == '__main__':
    sys.exit(main())