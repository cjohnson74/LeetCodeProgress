# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # bfs the tree
        # if root is equal to subRoot
            # dfs subRoot and root to compare each node
        # if a subtree is found return true
        # return False at end if not found
        
        stack = deque([root])
        
        while stack:
            for i in range(len(stack)):
                node = stack.pop()
                if node.val == subRoot.val:
                    if self.dfs(node, subRoot): return True
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                    
        return False
    
    def dfs(self, pNode, qNode):
        if not pNode and not qNode:
            return True
        
        if not pNode or not qNode or pNode.val != qNode.val:
            return False
        
        return self.dfs(pNode.left, qNode.left) and self.dfs(pNode.right, qNode.right)