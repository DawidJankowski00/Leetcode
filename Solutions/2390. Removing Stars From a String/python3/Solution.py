from collections import deque


class Solution:
    def removeStars(self, s: str) -> str:
        queue = deque()
        for v in s:
            if v == "*":
                queue.pop()
            else:
                queue.append(v)
        return "".join(queue)