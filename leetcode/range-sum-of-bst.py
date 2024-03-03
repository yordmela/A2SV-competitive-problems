# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # inorder traversal
        ans=[]
        def Inorder(root):
            
            if not root:
                return None
            Inorder(root.left)
            if root.val<=high and root.val>=low:
                ans.append(root.val)
            Inorder(root.right)
            
        Inorder(root)
        return  sum(ans)