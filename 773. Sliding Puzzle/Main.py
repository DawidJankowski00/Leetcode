from collections import deque
import copy
import sys
from typing import List
def main():
    sol = Solution()
    print(sol.slidingPuzzle([[4,1,2],[5,0,3]]))

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        queue = deque()
        queue.append([board, self.getPosition(board), 0])
        target = [[1,2,3],[4,5,0]]
        visited = set()
        visited.add(str(board))

        while queue:
            b, p, state = queue.popleft()
            if b == target:
                return state
            tmp = self.findSlide(b, p)
            print(b)
            print(p)
            print(tmp)
            print("\n")
            for item in tmp:
                if str(item[0]) not in visited:

                    visited.add(str(item[0]))
                    queue.append([item[0], item[1], state+1])

                    

        return -1
    def getPosition(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    return [i, j]
                
    def findSlide(self, board, position):
        result = []
        if position[0] == 0:
            match position[1]:
                case 0:
                    result.append(self.slide(board, position, "D"))
                    result.append(self.slide(board, position, "R"))
                case 1:
                    result.append(self.slide(board, position, "L"))
                    result.append(self.slide(board, position, "D"))
                    result.append(self.slide(board, position, "R"))
                case 2:
                    result.append(self.slide(board, position, "D"))
                    result.append(self.slide(board, position, "L"))
        if position[0] == 1:
            match position[1]:
                case 0:
                    result.append(self.slide(board, position, "U"))
                    result.append(self.slide(board, position, "R"))
                case 1:
                    result.append(self.slide(board, position, "L"))
                    result.append(self.slide(board, position, "U"))
                    result.append(self.slide(board, position, "R"))
                case 2:
                    result.append(self.slide(board, position, "U"))
                    result.append(self.slide(board, position, "L"))
        return result
                
    def slide(self, board, position, direction):
        result = copy.deepcopy(board)
        way = {
            "L": [0, -1],
            "R": [0, 1],
            "U": [-1, 0],
            "D": [1, 0]
        }
        result[position[0]][position[1]], result[position[0] + way[direction][0]][position[1] + way[direction][1]] = result[position[0] + way[direction][0]][position[1] + way[direction][1]], result[position[0]][position[1]]
        return result, [position[0] + way[direction][0], position[1] + way[direction][1]]

            


        

if __name__ == '__main__':
    sys.exit(main())