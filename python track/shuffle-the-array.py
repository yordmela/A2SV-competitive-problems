class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr=[]
        x,y=0,n
        while (y<2*n):
            arr.append(nums[x])
            arr.append(nums[y])
            x+=1
            y+=1
        return arr



        