class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count={}
        ans=[]
        for i in range(len(nums)):
            count[nums[i]]= 1+ count.get(nums[i],0)
        occurence= floor(len(nums)/3)
        for i in range(len(nums)):
            if count[nums[i]]>occurence and nums[i] not in ans:
                ans.append(nums[i])
        

        return ans
            
        