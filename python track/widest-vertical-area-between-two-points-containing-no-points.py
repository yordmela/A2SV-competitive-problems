class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        maxVertical=0
        for i in range(len(points)-1):
            if points[i][0]!=points[i+1][0]:
                maxVertical=max(points[i+1][0]-points[i][0], maxVertical)
        return maxVertical

