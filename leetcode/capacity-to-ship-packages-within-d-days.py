class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
       def check(mid):
            day=1
            sums=0
            for w in weights:
                sums+=w
                if sums>mid:
                    sums=w
                    day+=1
            return day<=days

       low,high=max(weights),sum(weights)
       while low<=high:
            mid= low+(high-low)//2
            if check(mid):
                high=mid-1
            else:
                low=mid+1
       return low