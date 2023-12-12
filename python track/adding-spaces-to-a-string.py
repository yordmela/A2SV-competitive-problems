class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        sentence=""
        set1 = set(spaces)
        for i in range(len(s)):
            if i in set1:
                sentence+=" "
            sentence+=s[i]
        return sentence
        