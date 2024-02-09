class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def prefixProduct(arr):
            new=[1]*(len(arr)+1)
            accu=1
            for i in range(len(arr)):
                new[i]= accu
                accu*=arr[i]
            new[-1]= accu
            return new
        reverseNum= list(reversed(nums))
        prefixProduct1= prefixProduct(nums)
        prefixProduct2= prefixProduct(reverseNum)
        prefixProduct2.reverse()
        ans=[0]*len(nums)
        for i in range(len(prefixProduct1)-1):
            ans[i]+=prefixProduct1[i]*prefixProduct2[i+1]
        return ans

            
       