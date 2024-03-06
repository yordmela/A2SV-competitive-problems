class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix=[0]*len(nums)
        for r in requests:
            if r[1]!=len(nums)-1:
                prefix[r[1]+1]-=1
            prefix[r[0]]+=1
        accu=0
        for i in range(len(prefix)):
            accu+=prefix[i]
            prefix[i]=accu
        nums.sort()
        prefix.sort()
        ans=0
        for i in range(len(prefix)):
            ans+=prefix[i]*nums[i]
        return ans%(10**9+7)
