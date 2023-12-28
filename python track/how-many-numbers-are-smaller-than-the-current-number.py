class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans=[]
        arranged= sorted(nums)
        for num in nums:
            ans.append(len(nums[0:arranged.index(num)]))
        return ans
        