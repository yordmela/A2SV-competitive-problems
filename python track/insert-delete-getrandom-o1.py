class RandomizedSet:

    def __init__(self):
        self.numSet=set()
        self.arr=[]
        

    def insert(self, val: int) -> bool:
        if val not in self.numSet:
            self.numSet.add(val)
            self.arr.append(val)
            return True
        return False

        

    def remove(self, val: int) -> bool:
        if val in self.numSet:
            self.numSet.remove(val)
            self.arr.remove(val)
            return True
        return False
        

    def getRandom(self) -> int:
        randomNum= random.randint(0,len(self.arr)-1)
        return self.arr[randomNum]

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()