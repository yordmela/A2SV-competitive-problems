class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        dic=defaultdict(list)
        for i,num in enumerate(nums):
            dic[num].append(i)
       
        
        arr=[0]*len(nums)
        for i in dic:
            left=0
            if len(dic[i])>1:
                total=sum(dic[i])
                for k in range (len(dic[i])):
                    arr[dic[i][k]]= (dic[i][k]*k-left+ (total-left-dic[i][k]))-(dic[i][k]*(len(dic[i])-1-k))
                    left+=dic[i][k]
        return arr