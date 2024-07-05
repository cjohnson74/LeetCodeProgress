# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        remaining = targetSum - root.val
        if remaining == 0 and root.left is None and root.right is None:
            return True
        
        leftTree = self.hasPathSum(root.left, remaining)
        rightTree = self.hasPathSum(root.right, remaining)
        
        if leftTree or rightTree:
            return True
        
        return False