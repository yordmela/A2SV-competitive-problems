class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        noOfIcecream=0
        for i in range(len(costs)):
            if coins>= costs[i]:
                coins-=costs[i]
                noOfIcecream+=1
            else:
                break
        return noOfIcecream
        