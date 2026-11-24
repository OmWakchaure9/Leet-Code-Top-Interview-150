import random

class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.indexMap = {}

    def insert(self, val):
        if val in self.indexMap:
            return False

        self.indexMap[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val):
        if val not in self.indexMap:
            return False

        idx = self.indexMap[val]
        last = self.nums[-1]

        self.nums[idx] = last
        self.indexMap[last] = idx

        self.nums.pop()
        del self.indexMap[val]

        return True

    def getRandom(self):
        return random.choice(self.nums)
