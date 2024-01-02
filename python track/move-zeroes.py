class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        seeker,placeholder=0,0
        while seeker<len(nums):
            if nums[seeker]!=0 and nums[placeholder]==0:
                nums[seeker],nums[placeholder]=nums[placeholder],nums[seeker]
                placeholder+=1
            elif nums[placeholder]!=0:
                placeholder+=1
            seeker+=1
        return nums