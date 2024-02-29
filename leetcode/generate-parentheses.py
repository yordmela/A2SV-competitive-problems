class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only if the number of open parenthesis is > close that we can add a closing parethesis
        # when open==close==n we stop adding paren.
        # add open if open<n

        stack=[]
        ans=[]
        def backtracking(open, close):
            #base case
            if open==close==n:
                ans.append(''.join(stack))
                return
            if open<n:
                stack.append('(')
                backtracking(open+1,close)
                stack.pop()
            if open>close:
                stack.append(')')
                backtracking(open, close+1)
                stack.pop()
            
        backtracking(0,0)
        return ans