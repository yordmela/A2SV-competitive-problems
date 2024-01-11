class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
       l=0
       maxone=0
       zero=1
       if 0 not in nums:
           return len(nums)-1
       for r in range(len(nums)):
           if nums[r]==0:
               zero-=1
           while zero<0:
               if nums[l]==0:
                   zero+=1
               l+=1
           maxone=max(maxone,r-l)
       return maxone

           
