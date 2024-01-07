class Solution(object):
    def findMaxAverage(self, nums, k):
        l=0
        cursum, maxsum= 0,float('-inf')
        for r in range (len(nums)):
            cursum+=nums[r]
            if r-l+1==k:
                maxsum= max(maxsum, cursum)
                cursum-=nums[l]
                l+=1
        maxave= float(maxsum)/float(k)
        return maxave
       


        
        