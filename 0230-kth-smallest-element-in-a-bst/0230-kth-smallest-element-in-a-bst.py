# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def inorderTraversal(root, vals):
            if root:
                inorderTraversal(root.left, vals)
                vals.append(root.val)
                inorderTraversal(root.right, vals)
            
        inorderList = []
        inorderTraversal(root, inorderList)
        
        return inorderList[k-1]
            