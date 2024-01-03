class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        
        maximum=0
        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[i])-1):
               sums=0
               sums+=grid[i][j]
               sums+=sum(grid[i+1][j-1:j+2])
               sums+=sum(grid[i-1][j-1:j+2])
               maximum= max(sums,maximum)
        return maximum
               
