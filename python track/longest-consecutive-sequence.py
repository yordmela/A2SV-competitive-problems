class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet= set(nums)
        longest=0
        for num in nums:
            if num-1 not in hashSet:
                length=0
                while num+length in hashSet:
                    length+=1
                longest=max(length,longest)
        return longest
                