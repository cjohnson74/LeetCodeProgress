# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, depth = 1):
            if not node:
                return 0
            
            leftDepth = dfs(node.left, depth + 1) if node.left else depth
            rightDepth = dfs(node.right, depth + 1) if node.right else depth
            
            return max(leftDepth, rightDepth)
        
        return dfs(root)