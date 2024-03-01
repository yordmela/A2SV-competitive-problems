class Solution:
    def minimumSteps(self, s: str) -> int:
        pt=len(s)-1
        zeros=0
        ans=0
        while pt>=0:
            if s[pt]=='0':
                zeros+=1
            else:
                ans+=zeros
            pt-=1
        return ans