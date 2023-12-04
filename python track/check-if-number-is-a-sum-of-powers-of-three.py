class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
      ternary=[]
      while n/3!=0:
          ternary.append(n%3)
          n=n//3
      if 2 in ternary:
          return False
      return True
          


        