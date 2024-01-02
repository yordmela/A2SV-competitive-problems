
class Solution:
        def validMountainArray(self, arr: List[int]) -> bool:
            if len(arr)<3:
                return False
            less, greater=[],[]
            i=0
            for i in range (len(arr)-1):
                if arr[i]==arr[i+1]:
                    return False
                if arr[i]>arr[i+1]:
                    break
                less.append(arr[i])
            for k in range (i,len(arr)):
                greater.append(arr[k])
            if len(greater)==0 or len(less)==0:
                return False
            for k in range(len(less)-1):
                if less[k]>=less[k+1]:
                    return False
            for k in range(len(greater)-1):
                if greater[k]<=greater[k+1]:
                    return False
            return True
             
                
            
            