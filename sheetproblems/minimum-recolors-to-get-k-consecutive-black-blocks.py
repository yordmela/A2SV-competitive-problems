class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        dic=defaultdict(int)
        l=0
        minoperation=len(blocks)
        if "W" not in blocks:
            return 0
        for r in range(len(blocks)):
            dic[blocks[r]]+=1
            if r>=k-1:
                minoperation=min(dic["W"],minoperation)
                dic[blocks[l]]-=1
                l+=1
            print(r,dic)
        return minoperation
