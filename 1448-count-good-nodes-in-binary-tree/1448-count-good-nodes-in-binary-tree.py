# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, greatestVal):
            count = 0
            if not root:
                return count
            
            if root.val >= greatestVal:
                return 1 + dfs(root.right, root.val) + dfs(root.left, root.val)
            else:
                return dfs(root.left, greatestVal) + dfs(root.right, greatestVal)
        
        return dfs(root, root.val) 