class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        maximum=0
        ones=0
        count=0
        for i in range(len(flips)):
            maximum=max(maximum,flips[i])
            ones+=1
            if maximum==ones:
                count+=1
        return count


        