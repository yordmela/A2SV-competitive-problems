class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic={}
        for num in arr1:
            dic[num]= 1+ dic.get(num, 0)
        pointer=0
        res=[]
        set1 = set(arr2)
        for i in range(len(arr2)):
            for j in range(dic[arr2[i]]):
                res.append(arr2[i])
                pointer+=1
        res1 = []
        for i in range(len(arr1)):
            if arr1[i] not in set1:
                res1.append(arr1[i])
        res1.sort()
        return res + res1
                
        return arr1
        
        