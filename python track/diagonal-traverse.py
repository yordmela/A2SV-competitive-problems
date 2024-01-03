class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        def check(a,b):
            if a>=0 and a<len(mat) and b>=0 and b<len(mat[0]):
                return True
        up=True
        ans=[]
        ans.append(mat[0][0])
        curr=[0,0]
        while curr != [len(mat)-1,len(mat[0])-1]:
            if up:
                if check(curr[0]-1,curr[1]+1):
                    curr = [curr[0]-1,curr[1]+1]
                    ans.append(mat[curr[0]][curr[1]])
                   
                elif check(curr[0], curr[1]+1):
                     curr = [curr[0],curr[1]+1]
                     ans.append(mat[curr[0]][curr[1]])
                     up=False
                elif check(curr[0]+1, curr[1]):
                     curr = [curr[0]+1,curr[1]]
                     ans.append(mat[curr[0]][curr[1]])
                     up=False
            else:
                if check(curr[0]+1, curr[1]-1):
                     curr = [curr[0]+1,curr[1]-1]
                     ans.append(mat[curr[0]][curr[1]])
                elif check(curr[0]+1, curr[1]):
                     curr = [curr[0]+1,curr[1]]
                     ans.append(mat[curr[0]][curr[1]])
                     up=True
                elif check(curr[0], curr[1]+1):
                     curr = [curr[0],curr[1]+1]
                     ans.append(mat[curr[0]][curr[1]])
                     up=True
        return ans
                


