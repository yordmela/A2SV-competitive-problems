class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        # we keep the left sum and we find the right sum from the total- left then 
        # the rightSum-currNum*noOfelementsInTheRight + currNum*noOfelementsInTheLeft-leftSum gives the absolute diffrence

        total=sum(nums)
        left=0
        ans=[]
        for i,n in enumerate(nums):
            right=total-n-left
            absDiff= ((i*n)-left) + (right-((len(nums)-i-1)*n))
            ans.append(absDiff)
            left+=n
        return ans