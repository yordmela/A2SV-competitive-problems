class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans=[]
        evenSum=sum(num for num in nums if num%2==0)
        for query in queries:
            if nums[query[1]]%2!=0 and query[0]%2!=0:
                nums[query[1]]+=query[0]
                evenSum+=nums[query[1]]
            elif nums[query[1]]%2==0 and query[0]%2!=0:
                evenSum-=nums[query[1]]
                nums[query[1]]+=query[0]
            elif nums[query[1]]%2==0 and query[0]%2==0:
                evenSum+=query[0]
                nums[query[1]]+=query[0]
            else:
                nums[query[1]]+=query[0]
            ans.append(evenSum)
        return ans