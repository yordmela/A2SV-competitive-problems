class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
       if destination<start:
          return min(sum(distance[destination:start]), sum(distance[start:]) + sum(distance[:(destination-len(distance))]))

       
       return min(sum(distance[start:destination]), sum(distance[destination:])+sum(distance[:(start-len(distance))]))

        