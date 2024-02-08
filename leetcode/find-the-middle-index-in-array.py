class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix_sum=[0]*(len(nums)+1)
        accumulator=0
        for i in range(len(nums)):
            prefix_sum[i]=accumulator
            accumulator+=nums[i]
        prefix_sum[-1]=accumulator
        
        for i in range(len(nums)):
            if prefix_sum[i]== prefix_sum[-1]-prefix_sum[i+1]:
                return i
        return -1
        