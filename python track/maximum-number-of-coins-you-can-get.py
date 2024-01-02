class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        l,r=0,len(piles)-2
        maxPile=0
        while l<r:
            maxPile+=piles[r]
            l+=1
            r-=2
        return maxPile

        