class Solution:
    def printVertically(self, s: str) -> List[str]:
        maxWord=0
        count=0
        for i in range(len(s)):
            if s[i].isalpha():
                count+=1
            else:
                count=0
            maxWord= max(maxWord, count)
        arr=[""]*maxWord
        p=0
        while p<len(s):
           for i in range(maxWord):
               if p<len(s) and s[p].isalpha() :
                   arr[i]+=s[p]
                   p+=1
               else:
                   arr[i]+=" "
           p+=1
        for i in range(len(arr)):
            arr[i]=arr[i].rstrip()
        return arr
              

