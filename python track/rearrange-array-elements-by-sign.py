class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive=[]
        negative=[]
        ans=[]
        for i in range(len(nums)):
            if nums[i]<0:
                negative.append(nums[i])
            else:
                positive.append(nums[i])
        for i in range(len(positive)):
            ans.append(positive[i])
            ans.append(negative[i])
        return ans

             
                
               
           
     
            
            
        