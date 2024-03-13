class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans= nums[0]
        total=0
        for i in range(len(nums)):
            total+=nums[i]
            oper= ceil(total/(i+1))
            ans= max(ans,oper)
        return ans