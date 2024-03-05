class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        l,r=0,len(nums)-1
        ans=0
        while l<r:
            if nums[l]+nums[r]<target:
                ans+=r-l
                l+=1
                # while nums[l-1]==nums[l]:
                #     l+=1
            else:
                r-=1
               
        return ans
