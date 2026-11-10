from collections import deque
import random
from typing import List

class RandomizedSet:
    
    def __init__(self):
        self.mySet = {}
    def insert(self, val: int) -> bool:
        if val in self.mySet:
            return False
        else:
            self.mySet[val] = 1
            return True

    def remove(self, val: int) -> bool:
        if val in self.mySet:
            del self.mySet[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(list(self.mySet.keys()))
