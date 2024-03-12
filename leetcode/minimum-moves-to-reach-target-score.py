class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans=0
        while target!=1:
            if target%2==0 and maxDoubles:
                target=target//2
                maxDoubles-=1
            elif not maxDoubles:
                ans+=target-2
                target=1
            else:
                target-=1
            ans+=1
        return ans
            