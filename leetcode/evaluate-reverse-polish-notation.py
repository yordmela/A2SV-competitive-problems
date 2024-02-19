class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]       

        for val in tokens:
            if val!='/' and val!='*' and val!='+' and val!='-':
                stack.append(val)
            elif stack:
               val1=stack.pop()
               val2=stack.pop()
               stack.append(str(trunc(eval(val2 + val + val1) )))
                
        return int(stack[-1])
       


                
        