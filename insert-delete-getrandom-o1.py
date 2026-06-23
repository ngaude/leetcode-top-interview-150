import random

class RandomizedSet:

    def __init__(self):
        self.d = {}
        self.l = []

    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        self.d[val] = len(self.l)
        self.l.append(val)
        return True

    def remove(self, val: int) -> bool:
        if not val in self.d:
            return False
        i = self.d[val]
        self.l[i] = self.l[-1]
        self.d[self.l[-1]] = i
        self.l.pop()
        self.d.pop(val)
        return True

    def getRandom(self) -> int:
        if len(self.l) > 1:
            i = random.randint(0,len(self.l)-1)
            return self.l[i]
        else:
            return self.l[0]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()



s = RandomizedSet()
s.insert(0)
s.insert(1)
s.remove(0)
s.insert(2)
s.remove(1)
assert s.getRandom() == 2
