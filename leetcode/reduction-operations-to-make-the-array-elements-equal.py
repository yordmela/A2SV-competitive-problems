class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        operation=0
        count=0
        nums.sort(reverse=True)
        for r in range(len(nums)-1):
            count+=1
            if nums[r]!=nums[r+1]:
                operation+=count
        return operation
