class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic= defaultdict(int)
        for char in s:
            dic[char]+=1
        ans=0
        
        flag=False
        for char in dic:
            if dic[char]%2 and not flag:
                ans+=dic[char]- (dic[char]%2)+1
                flag=True
            else:
                ans+=dic[char]- (dic[char]%2)
            
        return ans