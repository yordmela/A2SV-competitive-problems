from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue=deque([])
        count=0
        for i in range(len(tickets)):
            queue.append([tickets[i],i])
        
        while queue:
           
            popeditem, popedindex=  queue.popleft()
            popeditem-=1
            if popeditem!=0:
                queue.append([popeditem, popedindex])
            count+=1
            if popedindex==k and popeditem==0:
                break
        return count

            