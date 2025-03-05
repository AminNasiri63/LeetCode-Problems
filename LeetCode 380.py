import random
class RandomizedSet:

    def __init__(self):
        self.newSet = set()
        

    def insert(self, val: int):
        if val in self.newSet:
            return False
        else:
            self.newSet.add(val)
            return True    

    def remove(self, val: int):
        if val in self.newSet:
            self.newSet.remove(val)
            return True
        else:
            return False        

    def getRandom(self):
        idSet = random.randint(0, len(self.newSet)-1)
        return list(self.newSet)[idSet]