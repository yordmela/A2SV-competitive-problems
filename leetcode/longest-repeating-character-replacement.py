class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic={}
        l,r=0,0
        max_sub=0
        while r<len(s):
            dic[s[r]]=1+dic.get(s[r],0)
            max_freq= dic[max(dic, key=dic.get)]
            while (r-l+1)-max_freq>k:
                dic[s[l]]-=1
                if dic[s[l]]==0:
                    dic.pop(s[l])
                l+=1
            max_sub= max(max_sub, r-l+1)
            r+=1
        
        return max_sub
            
