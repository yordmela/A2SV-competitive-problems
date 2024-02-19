class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack=[]
        start=[0]*len(arr)
        end=[len(arr)]*len(arr)
        # find the starting and the end where i is small
        for i in range(len(arr)):
            while stack and arr[stack[-1]]>arr[i]:
                end[stack[-1]]= i
                stack.pop()
            if stack:
               start[i]=stack[-1]
            else:
                start[i]=-1
            stack.append(i)
        # find the sum of the minimum number using the one to the right of it times the one on the left times the number itself
        ans=0
        for i in range(len(arr)):
            ans+= ((i-start[i])* (end[i]-i))*arr[i]
            print(ans)
        return ans%(10**9 + 7)