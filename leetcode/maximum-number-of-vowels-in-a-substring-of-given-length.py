class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count=0
        maxcount=0
        l,r=0,0
        vowel={'a','e','i','o','u'}
        for r in range(k):
            if s[r] in vowel:
                count+=1
        r+=1
        maxcount=max(maxcount, count)
        while r<len(s):
           
            if s[l] in vowel:
                count-=1
            l+=1
            
            if s[r] in vowel:
                count+=1
            r+=1
            maxcount=max(maxcount, count)
        return maxcount


        