class Solution:
    def sortColors(self, nums: List[int]) -> None:
        arr=[0]*3
        for i in range(len(nums)):
            arr[nums[i]]+=1
        target=0
        for i in range(3):
            for j in range(arr[i]):
                nums[target]=i
                target+=1
        return nums


            
        