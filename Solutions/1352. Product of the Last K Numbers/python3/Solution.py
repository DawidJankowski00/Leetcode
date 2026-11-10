from typing import List

class ProductOfNumbers:

    def __init__(self):
        self.stream = []
        self.prod = 1

    def add(self, num: int) -> None:
        if num == 0:
            self.stream = []
            self.prod = 1
        else:
            self.prod *= num
            self.stream.append(self.prod)

    def getProduct(self, k: int) -> int:
        if len(self.stream) < k:
            return 0
        if len(self.stream) == k:
            return self.stream[-1]
        return self.stream[-1] // self.stream[-k -1]
