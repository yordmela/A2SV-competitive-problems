class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        mindiffer=float('inf')
        ans=0
        for i in range(len(nums)):
            l,r=i+1, len(nums)-1
            while l<r:
                sums= nums[i]+nums[l]+nums[r]
                if sums==target:
                    return target
                elif sums<target:
                    l+=1
                elif sums>target:
                    r-=1
                differ= abs(sums-target)
                if mindiffer>differ:
                    mindiffer=differ
                    ans= sums
        return ans