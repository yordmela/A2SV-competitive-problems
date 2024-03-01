class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        runingSum= 0
        minm= 0
        maxi= nums[0]

        for num in nums:
            runingSum+=num
            maxi= max(maxi, runingSum-minm)
            minm= min(minm, runingSum)
        return maxi
