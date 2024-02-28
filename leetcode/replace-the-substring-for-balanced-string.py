class Solution:
    def balancedString(self, s: str) -> int:
        dic={}
        for i in range(len(s)):
            dic[s[i]]=1+dic.get(s[i],0)
        occur= len(s)//4
        extra={}
        for i in dic:
            if dic[i]>occur:
                extra[i]= dic[i]-occur
        if not extra:
            return 0
        distinct= len(extra)
        l,r=0,0
        min_subarray=len(s)
        while r<len(s):
            if s[r] in extra:
                extra[s[r]]-=1
                if extra[s[r]]==0:
                    distinct-=1
          
            #ower shrinking conditions are to when distinct is equal to 0 which means all our extras are within our subarray
            while distinct==0:
                min_subarray= min(min_subarray, r-l+1)
                if s[l] in extra:
                    extra[s[l]]+=1
                    if extra[s[l]]>0: distinct+=1
                l+=1
            r+=1
        return min_subarray