class Solution:
    def largestGoodInteger(self, num: str) -> str:
        substring= ["000","111","222","333","444","555", "666","777", "888","999"]
        ans=""
        for sub in substring:
            if sub in num:
                ans=sub
        return ans
            


        