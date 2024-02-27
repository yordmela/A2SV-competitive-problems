class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dic={}
        l,r=0,0
        maxFruit=0
        while r<len(fruits):
            if len(dic)<2 or fruits[r] in dic:
                dic[fruits[r]]= 1+ dic.get(fruits[r],0)
            else:
                while len(dic)==2:
                    dic[fruits[l]]-=1
                    if dic[fruits[l]]==0:
                        dic.pop(fruits[l])
                    l+=1
                dic[fruits[r]]= 1+ dic.get(fruits[r],0)
            maxFruit= max(maxFruit, r-l+1)
            r+=1
        return maxFruit