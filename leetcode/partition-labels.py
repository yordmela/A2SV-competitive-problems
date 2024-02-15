class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # a function to merge the start,end indicies
        def merge(intervals):
            intervals.sort(key=lambda x:x[0])
            merged=[]
            for interval in intervals:
                if not merged or interval[0]>merged[-1][1]:
                    merged.append(interval)
                elif merged[-1][0]<=interval[0]<=merged[-1][1]:
                    merged[-1][1]= max(merged[-1][1], interval[1])
            return merged




        # find and store the start and the end indicies in a dic
        arr=[]
        reverseS= s[::-1]
        start, end=0,0
        hashSet=set()
        for chars in s:
            if chars not in hashSet:
                arr.append([s.index(chars), len(s)-1-reverseS.index(chars)])
                hashSet.add(chars)

           
       
        # find the partition from the merged array
        merged= merge(arr)  
        ans=[]
        for item in merged:
            ans.append(item[1]-item[0]+1)
        return ans
      
            
