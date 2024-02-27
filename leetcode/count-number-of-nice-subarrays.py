class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
       l,r=0,0
       odd,ans,cnt=0,0,0
       while r<len(nums):
           if nums[r]%2:
               odd+=1
               cnt=0
           while odd==k:
               cnt+=1
               if nums[l]%2:
                   odd-=1
               l+=1
           ans+=cnt
           r+=1
       return ans
       