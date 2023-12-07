class Solution:
    def totalMoney(self, n: int) -> int:
        sums=0
        if n<=7:
            return sum(range(1,n+1))
        for i in range(n//7):
            sums+=28+i*7
        sums+=sum(range(n//7+1, n%7+(n//7)+1))
        return sums
                



        