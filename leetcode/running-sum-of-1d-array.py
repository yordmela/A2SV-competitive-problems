class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefixSum=[0]*len(nums)
        accumulator=0
        for i in range(len(nums)):
            accumulator+=nums[i]
            prefixSum[i]=accumulator
        return prefixSum