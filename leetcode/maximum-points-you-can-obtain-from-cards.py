class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total=sum(cardPoints)
        win_size= len(cardPoints)-k
        l,r=0,0
        win_sum=0
        score=0
        if k==len(cardPoints):
            return total
        while r< len(cardPoints):
            win_sum+=cardPoints[r] 
            if r>=win_size-1:
                score= max(score, total-win_sum)
                win_sum-=cardPoints[l]
                l+=1
            r+=1
        
        return score