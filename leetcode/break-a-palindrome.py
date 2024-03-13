class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        temp= list(palindrome)
        palindrome= list(palindrome)
        if len(palindrome)==1:
            return ""
        
        for i in range(len(palindrome)):
            if palindrome[i]!="a":
                palindrome[i]="a"
                break

        flag=False
        for char in palindrome:
            if char!="a" :
                flag=True
                break
    
        if not flag:
            temp[-1]="b"
            return "".join(temp)
        return "".join(palindrome)