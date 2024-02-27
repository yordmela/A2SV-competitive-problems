# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic={}
        def inorder(node):
            if node==None:
                return None
            inorder(node.left)
            dic[node.val]= 1+ dic.get(node.val,0)
            inorder(node.right)
        inorder(root)
        ans=[]
        dic1={2:7,8:1}
        maxfreq= max(dic,key=dic.get)

        for i in dic:
            if dic[i]==dic[maxfreq]:
                ans.append(i)
        return ans