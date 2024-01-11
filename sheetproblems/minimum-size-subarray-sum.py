class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r=0,0
        sums=0
        minlen=float('inf')
        while r<len(nums):
            sums+=nums[r]
            while sums>=target:
                minlen=min(minlen, r-l+1)
                sums-=nums[l]
                l+=1
                
            r+=1
        if minlen==float('inf'):
            return 0
        return minlen
        