class Solution:
    def simplifyPath(self, path: str) -> str:
        files= path.split('/')
        while "" in files:
            files.remove("")
        stack=[]
        for char in files:
            if stack and char=="..":
                stack.pop()
            
            elif char!=".." and char!=".":
                stack.append(char)
        return "/"+"/".join(stack)
