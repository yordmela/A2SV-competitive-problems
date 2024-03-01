class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        dic={}
        l,r=0,0
        distinct= len(set(nums))
        count=0
        while r<len(nums):
            dic[nums[r]]=1+dic.get(nums[r],0)
           
            while len(dic)==distinct:
                count+=len(nums)-r
                dic[nums[l]]-=1
                if dic[nums[l]]==0:
                    dic.pop(nums[l])
                l+=1
            
            r+=1
        return count