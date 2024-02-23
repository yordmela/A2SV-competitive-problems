class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def pow(x,n):
            #base cases
            if x==0:
                return 0
            if n==0:
                return 1
            # recursive case
            res= pow(x, n//2)
            res= res*res
            return (x*res)%(10**9+7) if n%2 else res %(10**9+7)
        


        evens= (n//2)+ (n%2)
        odds= n//2
        
        return (pow(5,evens)*pow(4, odds))%(10**9+7)