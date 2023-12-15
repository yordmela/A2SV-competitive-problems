class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dic_winner={}
        dic_losser={}
        ans=[]
        for match in matches:
            dic_winner[match[0]]=1 + dic_winner.get(match[0],0)
            dic_losser[match[1]]=1 + dic_losser.get(match[1],0)
        winner=sorted([win for win in dic_winner if win not in dic_losser])
        losser=sorted([loss for loss in dic_losser if dic_losser[loss]==1 ])
        ans.append(winner)
        ans.append(losser)
        return ans
        