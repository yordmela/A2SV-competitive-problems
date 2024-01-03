class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        l,r=0,0
        count=0
        g.sort()
        s.sort()
        while r<len(s) and l<len(g):
            if g[l]>s[r]:
                r+=1
            else:
                l+=1
                r+=1
                count+=1
        return count

        