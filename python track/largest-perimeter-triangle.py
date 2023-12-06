class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        r=len(nums)-1
        l= r-2
        while l>=0:
            if nums[l]+nums[l+1]>nums[r]:
               return nums[l]+nums[l+1]+nums[r]

            else:
                l-=1
                r-=1
        return 0
                