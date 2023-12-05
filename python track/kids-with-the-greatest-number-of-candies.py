class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        arr=[0]*len(candies)
        maximum= max(candies)
        for i in range(len(arr)):
            if candies[i]+extraCandies>=maximum:
                arr[i]= True
            else:
                arr[i]=False
        return arr
        