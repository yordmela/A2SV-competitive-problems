class Solution:
    def smallestNumber(self, num: int) -> int:
       nums=[]
       if num>=0:
            for i in range(len(str(num))):
                nums.append(int(str(num)[i]))
       else:
            for i in range(1,len(str(num))):
                nums.append(int(str(num)[i]))
       print(nums)
       if len(nums)==1:
           return num
       if num>0:
           nums.sort()
       else:
           nums.sort(reverse=True)
       l,r=0,1
       while nums[0]==0 and r<len(nums):
           if nums[r]!=0:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
           elif nums[r]==0:
                r+=1
          
                
       print(nums)
       if num<0:
           return -1*int ("".join(map(str, nums)))
       else:
           return int ("".join(map(str, nums)))
       
           
                    
                    
        