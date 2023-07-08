# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # dfs
        # maxDiameter = 0
        # get the height of left and depth of right
        # currDiameter is 1 + heightLeft + heightRight
        
        maxDiameter = [0]
        
        def dfs(node):
            if not node:
                return -1
            
            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)
            
            maxDiameter[0] = max(maxDiameter[0], 2 + leftHeight + rightHeight)
            
            return 1 + max(leftHeight, rightHeight)
            
        dfs(root)
        return maxDiameter[0]