class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        retrieve= capacity
        ans=0
        for i in range(len(plants)):
            if capacity>=plants[i]:
                capacity-=plants[i]
                ans+=1
            else:
                ans+= 2*i+1
                capacity= retrieve-plants[i]
        return ans


        