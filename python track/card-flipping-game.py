class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        bad=set()
        minimumGood= max(max(fronts),max(backs))
        flag="False"
        for i in range(len(fronts)):
            if fronts[i]==backs[i]:
                bad.add(fronts[i])
        for i in range (len(fronts)):
            if fronts[i] not in bad : 
                minimumGood= min(fronts[i], minimumGood)
                flag="True"
            if backs[i] not in bad:
                minimumGood= min(backs[i], minimumGood)
                flag="True"

        if flag=="True":
            return minimumGood
        else:
            return 0


        
        