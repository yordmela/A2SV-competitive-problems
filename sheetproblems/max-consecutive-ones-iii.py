class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        dic= defaultdict(int)
        l=0
        maxones=0
        for r in range(len(nums)):
            dic[nums[r]]+=1
            while dic[0]>k:
                dic[nums[l]]-=1
                l+=1
            maxones=max(maxones, r-l+1)
            r+=1
        return maxones
                