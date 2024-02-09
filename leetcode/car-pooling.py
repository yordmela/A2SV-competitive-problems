class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        def findPrefixSum(arr):
            new=[0]*len(arr)
            accu=0
            for i in range(len(arr)):
                accu+=arr[i]
                new[i]=accu
            return new
        maxLoc=0
        for trip in trips:
            maxLoc=max(maxLoc, trip[-1])
        passangers= [0]*maxLoc
        for trip in trips:
            passangers[trip[1]]+= trip[0]
            if trip[-1]<len(passangers):
                passangers[trip[-1]]-= trip[0]
        allPassangers= findPrefixSum(passangers)
        for i in allPassangers:
            if i>capacity:
                return False
        return True