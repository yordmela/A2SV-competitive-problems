class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # determine our base case which hapens when rowIndex is 0 and 1 they will be [1] and [1,1]
        if rowIndex<=1:
            return [1]* (rowIndex+1)
        # we will state our recurrence relation which aims to get the base case
        prev_row= self.getRow(rowIndex-1)
        # now let's perform operations needed to get our current row- which starts and ends with 1
        curr_row=[1]
        for i in range(len(prev_row)-1):
            curr_row.append(prev_row[i]+prev_row[i+1])
        curr_row.append(1)
        return curr_row