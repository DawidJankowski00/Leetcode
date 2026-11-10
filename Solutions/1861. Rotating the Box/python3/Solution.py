from typing import List

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m = len(box)
        n = len(box[0])
        rotatedBox = [['.'] * m for _ in range(n)]

        for i in range(0, m):
            l = n-1
            r = n-1 
            while l>=0:
                if box[i][l] == "#":
                    box[i][l] = "."
                    box[i][r] = "#"
                    l -= 1
                    r -= 1
                elif box[i][l] == "*":
                    l -= 1
                    r = l
                else:
                    l -= 1
        for i in range(n):
            for j in range(m):
                rotatedBox[i][j] = box[m-1-j][i]
        return rotatedBox
