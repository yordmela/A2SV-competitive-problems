class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        flag=False
        for i in range (left, right+1):
            flag=False
            for rang in ranges:
                    if i in range (rang[0],rang[1]+1):
                        flag=True
                        break 
            if flag==False:
                return False 
                    
                   
           
        return flag

        