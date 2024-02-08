class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix
        self.prefix_sum=[[0 for _ in range(len(self.matrix[0]))] for _ in range(len(self.matrix))]
        self.prefix_sum[0][0]=self.matrix[0][0]
        for j in range(1,len(self.matrix[0])):
            self.prefix_sum[0][j]= self.prefix_sum[0][j-1]+self.matrix[0][j]
        for i in range(1,len(self.matrix)):
            self.prefix_sum[i][0]= self.prefix_sum[i-1][0]+self.matrix[i][0]
        for i in range(1, len(self.matrix)):
            for j in range(1, len(self.matrix[0])):
                self.prefix_sum[i][j]= self.prefix_sum[i-1][j]+self.prefix_sum[i][j-1]- self.prefix_sum[i-1][j-1]+self.matrix[i][j]
        print(self.prefix_sum)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1==0 and col1!=0:
            sums= self.prefix_sum[row2][col2]-self.prefix_sum[row2][col1-1]
        elif col1==0 and row1!=0:
            sums= self.prefix_sum[row2][col2]- self.prefix_sum[row1-1][col2]
        elif row1==0 and col1==0:
            sums= self.prefix_sum[row2][col2]
        else:
            sums= self.prefix_sum[row2][col2]- self.prefix_sum[row1-1][col2]-self.prefix_sum[row2][col1-1]+self.prefix_sum[row1-1][col1-1]
        return sums
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)