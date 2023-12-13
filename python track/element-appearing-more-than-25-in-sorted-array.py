class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        dic={}
        for i in range( len(arr)):
            dic[arr[i]]= 1+ dic.get(arr[i],0)
        for num in  dic:
            if dic[num]/len(arr)>0.25:
                return num


        