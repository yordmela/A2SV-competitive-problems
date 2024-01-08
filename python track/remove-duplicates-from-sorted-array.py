class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        l,r=0,1
        while r<len(nums):
            if nums[l]!=nums[r]:
                l+=1
                nums[l],nums[r]=nums[r], nums[l]
            r+=1
        return l+1