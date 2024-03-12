class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        ans=0
        for bracket in s:
            if stack and stack[-1]=="(" and bracket==")":
                stack.pop()
            elif bracket=="(":
                stack.append("(")
            else:
                ans+=1
        ans+=len(stack)
        return ans