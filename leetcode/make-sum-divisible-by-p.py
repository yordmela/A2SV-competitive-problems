class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        k=sum(nums)%p
        if not k :
            return 0
        curr=0
        ans=len(nums)
        dic={0:-1}
        for i,val in enumerate(nums):
            curr= (curr+val)%p
            target= (curr-k+p)%p
            if target in dic:
                ans= min(ans, i-dic[target])
            dic[curr]= i
        return ans if ans!=len(nums) else -1
        