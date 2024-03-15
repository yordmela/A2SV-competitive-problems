class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(mid):
            banana=0
            for pile in piles:
                banana+=ceil(pile/mid)
            return banana<=h
        low,high= 1,max(piles)
        while low<=high:
            mid=low+(high-low)//2
            if check(mid):
                high= mid-1
            else:
                low=mid+1
        return low