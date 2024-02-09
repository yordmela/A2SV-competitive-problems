class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum=[0]*(len(nums)+1)
        accu=0
        for i in range(len(nums)):
            prefix_sum[i]=accu
            accu+=nums[i]
        prefix_sum[-1]=accu
        #let's set a dictionary to check weather there are targetSum-the prefixSum
        dic= defaultdict(int)
        ans=0
        for i in range(len(prefix_sum)):
            if dic[prefix_sum[i]-goal]>0:
                ans+=dic[prefix_sum[i]-goal]
            dic[prefix_sum[i]]+=1
        return ans

        