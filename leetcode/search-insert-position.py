class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low,high= 0,len(nums)-1
        while low<=high:
            mid= low+(high-low)//2
            if nums[mid]>target:
                high= mid-1
            elif nums[mid]<target:
                low= mid+1
            else:
                return mid
        return low