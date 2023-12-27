class Bitset:

    def __init__(self, size: int):
       self.zeros=[0]*size
       self.ones=[1]*size
       self.counter=0

    def fix(self, idx: int) -> None:
        if self.zeros[idx]!=1:
             self.counter+=1
        self.zeros[idx]=1
        self.ones[idx]=0
       

    def unfix(self, idx: int) -> None:
        if self.zeros[idx]==1:
             self.counter-=1
        self.zeros[idx]=0
        self.ones[idx]=1
         
    def flip(self) -> None:
        self.counter= len(self.zeros)- self.counter
        x=self.zeros
        self.zeros= self.ones
        self.ones=x
      
        

    def all(self) -> bool:
        if self.counter==len(self.ones):
            return True
        return False
    def one(self) -> bool:
        if self.counter>0:
            return True
        return False

    def count(self) -> int:
        return self.counter

    def toString(self) -> str:
        return "".join(map(str,self.zeros))
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()