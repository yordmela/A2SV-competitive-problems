class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l,h= 0, len(letters)-1
        while l<=h:
            m=l+(h-l)//2
            if letters[m]>target:
                h=m-1
            else:
                l=m+1
        return letters[l] if l<len(letters) else letters[0]