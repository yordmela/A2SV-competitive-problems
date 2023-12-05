class Solution:
    def freqAlphabets(self, s: str) -> str:
        p=0
        ans=""
        while p<len(s):
            if p+2<len(s) and s[p+2]=="#":
                ans+=chr(int(s[p]+s[p+1])+96)
                p+=3
            else:
                ans+= chr(int(s[p])+96)
                p+=1
        return ans

        