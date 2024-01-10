class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        res=0
        dic=defaultdict(int)
        l=0
        for r in range(len(answerKey)):
            dic[answerKey[r]]+=1
            while min(dic["T"], dic["F"])>k:
                dic[answerKey[l]]-=1
                l+=1
            res=max(res, r-l+1)
        return res
                