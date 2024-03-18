class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        def check(mid):
            p1,p2=0,0
           
            while p1<len(houses):
                if p2>=len(heaters):
                    return False

                upperB=heaters[p2]+mid
                lowerB=heaters[p2]-mid
                if houses[p1]<lowerB:
                    return False
                
                if houses[p1]>upperB:
                    p2+=1
                else:
                    p1+=1
            return True
        
        low,high=0,10**9
        while low<=high:
            mid=low+(high-low)//2
            if check(mid):
                high=mid-1
            else:
                low=mid+1
        return low



                
