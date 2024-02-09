class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum=[0]*(len(nums)+1)
        accu=0
        for i in range(len(nums)):
            prefix_sum[i]=accu
            accu+=nums[i]
        prefix_sum[-1]= accu
        dic=defaultdict(int)
        ans=0
        for i in range(len(prefix_sum)):
            if dic[prefix_sum[i]%k] >0:
                ans+=dic[prefix_sum[i]%k]
            dic[prefix_sum[i]%k]+=1
        return ans