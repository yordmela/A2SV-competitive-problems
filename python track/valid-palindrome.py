class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        while l<r:
            if not s[l].isalnum(): 
                l+=1
               
            if not s[r].isalnum():
                 r-=1
            if s[l].isalnum() and s[r].isalnum() and s[l].lower()!=s[r].lower():
                    return False
            elif s[l].isalnum() and s[r].isalnum() and s[l].lower()==s[r].lower():
                l+=1
                r-=1
        return True
