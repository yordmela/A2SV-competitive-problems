class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        

        def rec(left,right,score_one,score_two,turn):
            if left > right:
                return score_one >= score_two
            
            if turn == 1:

                return rec(left+1,right,score_one+nums[left],score_two,2) or rec(left, right-1, score_one+nums[right], score_two,2 )
            if turn ==2:
                return rec(left+1,right,score_one,score_two+nums[left],1) and rec(left, right-1, score_one, score_two+nums[right],1 )
        
        return rec(0,len(nums)-1,0,0,1)