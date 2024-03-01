class Solution:
    def bestClosingTime(self, customers: str) -> int:
        prefixN=[0]
        sufixY=[0]

        no=0
        for i in range(len(customers)):
            if customers[i]=='N':
                no+=1
            prefixN.append(no)
        yes=0
        for i in range(len(customers)-1, -1,-1):
            if customers[i]=='Y':
                yes+=1
            sufixY.append(yes)
        
        
        sufixY.reverse()
        minm=float('inf')
        ans=0
        print(prefixN, sufixY)
        for i in range(len(prefixN)):
            if prefixN[i]+sufixY[i]<minm:
                minm = prefixN[i]+sufixY[i]
                ans= i
        return ans
