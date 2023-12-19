class Solution:
    def isHappy(self, n: int) -> bool:
        hashSet=set()
            
        while n not in hashSet:
            if n==1:
                return True
            hashSet.add(n)
            n= self.findSquareSum(n)
            
        return False
    def findSquareSum(self, n:int) -> int:
            squareSum=0
            while n:
                digit=n%10
                squareSum+=digit**2
                n=n//10
            return squareSum


            

        