# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, lowerBound, upperBound):
            if not root:
                return True
            if not (root.val > lowerBound and root.val < upperBound):
                return False
                
            return (dfs(root.left, lowerBound, root.val) and dfs(root.right, root.val, upperBound))
            
        return dfs(root, float('-inf'), float('inf'))
        
        