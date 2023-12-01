class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        string=""
        
        sorted_str= sorted(strs)
        first=sorted_str[0]
        last= sorted_str[-1]
        for i in range(len(sorted_str[0])):
            if first[i]!=last[i] :
                return string
            string+=first[i]
        return string
        

        