class Robot:

    def __init__(self, width: int, height: int):
        self.h= height
        self.w= width
        self.loc=[0,0]
        self.dir= "East"
        self.totalStep=0
    def step(self, num: int) -> None:
        h= self.h-1
        w= self.w-1
        temp1= num
        num= num%(2*(self.w-1+self.h-1))
        self.totalStep+=1

        while num:
            if self.dir=="East":
                self.loc[0]+=num
                temp= self.loc[0]
                if self.loc[0]>w:
                    self.loc[0]= w
                    num= temp- w
                    self.dir="North"
                else:
                    num=0
            elif self.dir=="North":
                self.loc[1]+=num
                temp=self.loc[1]
                if self.loc[1]>h:
                    self.loc[1]= h
                    num= temp-h
                    self.dir="West"
                    
                else:
                    num=0

                
            elif self.dir=="West":
                self.loc[0]-=num
                temp=self.loc[0]
                if self.loc[0]<0:
                    self.loc[0]=0
                    num=-temp
                    self.dir="South"
                else:
                    num=0
            elif self.dir=="South":
                self.loc[1]-=num
                temp=self.loc[1]
                if self.loc[1]<0:
                    self.loc[1]=0
                    num= -temp
                    self.dir="East"
                else:
                    num=0
        if temp1>0 and num==0 and self.loc==[0,0] and self.totalStep!=0:
            self.dir="South"
            

    def getPos(self) -> List[int]:
        return self.loc

    def getDir(self) -> str:
        return self.dir


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()