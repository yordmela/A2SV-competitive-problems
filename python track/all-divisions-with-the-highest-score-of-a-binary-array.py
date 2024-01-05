class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        dic = {}
        score=0
        ones=0
        ans=[]
        for i in range(len(nums)):
            if nums[i]==1:
                ones+=1
        score=ones
        dic[0]=score
        for i in range(len(nums)):
            if nums[i]==0:
                score+=1
            else:
                score-=1
            dic[i+1]=score
        maximum= max(dic.values())
        for n in dic:
            if dic[n]==maximum:
                ans.append(n)
        return ans
                