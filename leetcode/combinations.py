class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        def backtrack(curr,arr):
            #base case
            if len(arr)==k:
                ans.append(arr[:])
                return
            #recursive relation
            for next_num in range(curr, n+1):
                arr.append(next_num)
                backtrack(next_num+1, arr)
                arr.pop()
        backtrack(1,[])
        return ans