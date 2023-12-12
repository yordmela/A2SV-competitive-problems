class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        numHash={}
        for i in range (len(nums)):
            numHash[nums[i]]=i
        for operation in operations:
            if operation[0] in numHash:
                nums[numHash[operation[0]]]= operation[1]
                numHash[operation[1]]=numHash[operation[0]]
            
        return nums
            
        