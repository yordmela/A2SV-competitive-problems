class Solution:
    def maxScore(self, s: str) -> int:
        #changing the string to list
        arrS= list(map(int,s))
        #finding the prefix sum of the array to keep track of the 1's
        accu=0
        prefix_sum=[0]*(len(s))
        for i in range(len(arrS)):
            accu+=arrS[i]
            prefix_sum[i]=accu
        #calculate the 0's to the left plus the 1's to the right
        maxScore=0
        score=0
        zero=0
        for i in range(len(arrS)-1):
            if arrS[i]==0:
                zero+=1
            score= zero+ prefix_sum[-1]-prefix_sum[i]
            maxScore= max(score, maxScore)
        return maxScore

        
        