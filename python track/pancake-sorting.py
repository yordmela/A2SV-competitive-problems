class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans=[]
        r=len(arr)-1
        while r>0:
            if arr.index(max(arr[:r+1]))==0:
                arr[:r+1]= arr[:r+1][::-1]
                ans.append(r+1)
                r-=1
            else:
                ans.append(arr.index(max(arr[:r+1]))+1)
                arr[:arr.index(max(arr[:r+1]))+1]=arr[:arr.index(max(arr[:r+1]))+1][::-1]
                
        return ans
