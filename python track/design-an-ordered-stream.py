class OrderedStream:

    def __init__(self, n: int):
        self.orderedarr=[None]*n
        self.p=0
    def insert(self, idKey: int, value: str) -> List[str]:
        ans=[]
        self.orderedarr[idKey-1]=value
        if idKey-1>self.p:
            return []
        while self.p<len(self.orderedarr) and self.orderedarr[self.p]!=None:
            self.p+=1
        ans = self.orderedarr[idKey-1: self.p]

        return ans
            


            


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)