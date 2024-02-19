class Solution:
    def isValid(self, s: str) -> bool:
        dic={')':'(',  '}':'{',  ']':'['}
        stack=[]
        if s[0] in dic:
            return False
        for closeP in s:
            if closeP in dic:
                if stack and dic[closeP] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(closeP)
        if not stack:
            return True
        return False
            

        