class FrequencyTracker:
    
    def __init__(self):
        self.dic1=defaultdict(int)
        self.dic2=defaultdict(int)

        

    def add(self, number: int) -> None:
        self.dic1[number]+=1
        self.dic2[self.dic1[number]]+=1 
        self.dic2[self.dic1[number]-1]-=1 if self.dic2[self.dic1[number]-1]>0 else 0 

    def deleteOne(self, number: int) -> None:
         if self.dic1[number] > 0:
            self.dic2[self.dic1[number]] -= 1
            self.dic1[number] -= 1
            self.dic2[self.dic1[number]] += 1 
    def hasFrequency(self, frequency: int) -> bool:
        if frequency in self.dic2 and self.dic2[frequency]>0:
            return True
        else:
            return False
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)