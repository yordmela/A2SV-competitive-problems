class Solution:
    def reverseWords(self, s: str) -> str:
        ans=""
        l,r= len(s)-1, len(s)-1
        while l>=0:
            if s[l]==" " and s[r]!=" ":
                ans+=s[l+1:r+1]
                ans+=" "
                l-=1
                r=l
            elif s[r]==" ":
                r-=1
            l-=1
        ans+=s[0:r+1]
        ans = ans.strip()
        
        return ans