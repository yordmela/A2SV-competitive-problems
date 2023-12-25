class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=""
        ans=[]
        for i in range(len(digits)):
            num+=str(digits[i])
        num= str(int(num)+1)
        for i in range (len(num)):
            ans.append(int(num[i]))
        return ans
        