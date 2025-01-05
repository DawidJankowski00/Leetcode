import sys
import time
from typing import List
def main():
    sol = MinStack()
    start = time.time()
    print(sol.*****())
    print(time.time() - start)

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_elem = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_elem:
            val = min(self.min_elem[-1], val)
        self.min_elem.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_elem.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_elem[-1]

if __name__ == '__main__':
    sys.exit(main())