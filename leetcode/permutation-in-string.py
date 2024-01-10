class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dics1={}
        dics2={}
        l,r=0,0
        for char in s1:
            dics1[char]= 1+ dics1.get(char, 0)
        while r<len(s2):
            dics2[s2[r]]= 1+ dics2.get(s2[r], 0)
            print(dics2)
            if dics1==dics2:
                return True
            elif r-l+1>=len(s1):
                dics2[s2[l]]-=1
                if dics2[s2[l]]==0:
                    dics2.pop(s2[l])
                l+=1
            
            r+=1
        

        