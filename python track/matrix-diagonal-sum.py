class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sums=0
        primary={}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i==j or i+j==len(mat[0])-1:
                    sums+=mat[i][j]
        return sums
        