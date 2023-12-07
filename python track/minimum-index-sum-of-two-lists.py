class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        minindexSum= len(list1)+len(list2)
        ans=[]
        for i in range(len(list1)):
            if list1[i] in list2:
                minindexSum=min(minindexSum, i+ list2.index(list1[i]))
        for i in range(len(list1)):
            if list1[i] in list2 and i+list2.index(list1[i])==minindexSum:
                ans.append(list1[i])
        return ans
                

        