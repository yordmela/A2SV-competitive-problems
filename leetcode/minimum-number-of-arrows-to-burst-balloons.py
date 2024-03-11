class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points)==0:return 0
        points.sort()
        prev= points[0]
        ans=1
       
        print(points)
        for s,e in points[1:]:
            print(s,prev[1])
            if s>prev[1]:
                ans+=1
                prev= [s,e]
            else:
                prev[1]= min(e,prev[1])
        return ans
