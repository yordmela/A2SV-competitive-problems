class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def left(nums,target):
            low,high= 0,len(nums)-1
            while low<=high:
                mid= low+(high-low)//2
                if nums[mid]>=target:
                    high=mid-1
                else:
                    low=mid+1
            return low if low<len(nums) and nums[low]==target else -1
        def right(nums,target):
            low,high= 0,len(nums)-1
            while low<=high:
                mid= low+(high-low)//2
                if nums[mid]>target:
                    high= mid-1
                else:
                    low= mid+1
            return high if high>=0 and nums[high]==target else -1
        return [left(nums,target),right(nums,target)]

                
