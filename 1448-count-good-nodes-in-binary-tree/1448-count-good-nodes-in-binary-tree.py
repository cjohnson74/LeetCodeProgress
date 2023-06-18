# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, greatestVal):
            if not root:
                return 0
            
            count = 1 if root.val >= greatestVal else 0
            maxVal = max(greatestVal, root.val)
            count += dfs(root.left, maxVal)
            return count + dfs(root.right, maxVal)
        
        return dfs(root, root.val) 