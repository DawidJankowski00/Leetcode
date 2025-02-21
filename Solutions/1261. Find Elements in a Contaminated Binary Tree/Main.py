import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.*****())
    print(time.time() - start)

class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.tab = {}

        def rec(x, node: Optional[TreeNode]):
            if node.left != None:
                l = (2 * x) + 1
                self.tab[l] = True
                rec(l, node.left)
            if node.right != None:
                r = (2 * x) + 2
                self.tab[r] = True
                rec(r, node.right)
        if root != None:
            self.tab[0] = True
            rec(0, root)


    def find(self, target: int) -> bool:
        return target in self.tab

if __name__ == '__main__':
    sys.exit(main())