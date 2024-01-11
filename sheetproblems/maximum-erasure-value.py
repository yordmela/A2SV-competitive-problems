class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        dic=defaultdict(int)
        l,r=0,0
        sums=0
        maxsum=0
        while r<len(nums):
            
            sums+=nums[r]
            while nums[r] in dic:
                dic[nums[l]]-=1
                if dic[nums[l]]==0:
                    dic.pop(nums[l])
                sums-=nums[l]
                l+=1
            maxsum=max(maxsum, sums)
            dic[nums[r]]+=1
            r+=1
        return maxsum
        

            
        
