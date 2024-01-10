class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dicS={}
        dicP={}
        ans=[]
        l,r=0,0
        for char in p:
            dicP[char]=1+dicP.get(char,0)
        while r<len(s):
            dicS[s[r]]= 1+ dicS.get(s[r],0)
            
            
            if r>=len(p):
                dicS[s[l]]-=1
                if dicS[s[l]]==0:
                    dicS.pop(s[l])
                l+=1
            if dicS==dicP:
                ans.append(l)
            r+=1
        print(dicS)
        return ans

        
        