class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dic= defaultdict(int)
        for ans in answers:
            dic[ans]+=1
        res=0
        for i in dic:
            if i==0:
                res+=dic[i]
            else:
                times= ceil(dic[i]/(i+1))
                res+=times*(i+1)
        return res