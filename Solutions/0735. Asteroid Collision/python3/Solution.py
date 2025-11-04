from typing import Deque, List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for v in asteroids:
            while stack and stack[-1] > 0 and v < 0:
                if stack[-1] < -v:
                    stack.pop()
                    continue
                elif stack[-1] == -v:
                    stack.pop()
                break
            else:
                stack.append(v)
        return stack

