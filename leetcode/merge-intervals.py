class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        merged=[]
        for interval in intervals:
            if not merged or interval[0]>merged[-1][1]:
                merged.append(interval)
            elif merged[-1][0]<=interval[0]<=merged[-1][1]:
                merged[-1][1]= max(merged[-1][1], interval[1])
        return merged

            