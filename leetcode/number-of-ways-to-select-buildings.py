class Solution:
    def numberOfWays(self, s: str) -> int:
        prefix0=[0]*len(s)
        sufix0=[0]*len(s)
        prefix1=[0]*len(s)
        sufix1=[0]*len(s)
        ones,zeros=0,0
        for i in range(len(s)):
            if s[i]=='1':
                ones+=1
            else:
                zeros+=1
            prefix0[i]=zeros
            prefix1[i]=ones
        ones,zeros=0,0
        for i in range(len(s)-1,-1,-1):
            if s[i]=='1':
                ones+=1
            else:
                zeros+=1
            sufix0[i]=zeros
            sufix1[i]=ones
        ans=0
        for i in range(len(s)):
            if s[i]=='1':
                ans+= prefix0[i]*sufix0[i]
            else:
                ans+= prefix1[i]*sufix1[i]
        return ans
