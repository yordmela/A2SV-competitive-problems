class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        
        tasks.sort(reverse=True)
        processorTime.sort()
        pt=0
        ans=0
        for i in range(len(processorTime)):
            for n in range(4):
                ans= max(ans, processorTime[i]+tasks[pt])
                pt+=1
        return ans
                