class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x,n):
            #base cases
            if x==0:
                return 0
            if n==0:
                return 1
            # recursive case
            res= helper(x, n//2)
            res= res*res
            return x*res if n%2 else res
        ans= helper(x, abs(n))
        if n<0:
            return 1/ans
        return ans