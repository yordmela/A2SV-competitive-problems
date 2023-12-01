class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        x= (num-3)/3
        ans=[]
        if (num-3)%3==0:
            ans.append(int(x))
            ans.append(int(x+1))
            ans.append(int(x+2))
        return ans
        