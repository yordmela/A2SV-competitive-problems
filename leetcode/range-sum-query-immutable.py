class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.prefix=[0]*len(self.nums)
        self.accumulator=0
        for i in range(len(nums)):
            self.accumulator+=self.nums[i]
            self.prefix[i]= self.accumulator
        


        

    def sumRange(self, left: int, right: int) -> int:
        if left==0:
            return self.prefix[right]
        return self.prefix[right]-self.prefix[left-1]
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)