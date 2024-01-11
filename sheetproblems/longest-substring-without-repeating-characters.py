class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left=0
        charSet=set()
        res=0
        for right in range (len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left+=1
            charSet.add(s[right])
            res= max(res, right-left+1)
        return res



       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
            

        