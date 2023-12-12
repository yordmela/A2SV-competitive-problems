class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        before=[]
        after=[]
        middle=[]
        ans=[]
        for num in nums:
            if num>pivot:
                after.append(num)
            elif num<pivot:
                before.append(num)
            else:
                middle.append(num)
        ans.extend(before)
        ans.extend(middle)
        ans.extend(after)
        return ans
