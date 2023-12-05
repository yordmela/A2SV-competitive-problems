class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            if i%2!=0:
                for j in range(nums[i-1]):
                    ans.append(nums[i])
        return ans
        