"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}
        
        def dfs(node):
            oldToNew[node] = Node(node.val)
            
            for neighborNode in node.neighbors:
                if (neighborNode in oldToNew):
                    oldToNew[node].neighbors.append(oldToNew[neighborNode])
                else:
                    oldToNew[node].neighbors.append(dfs(neighborNode))
            
            return oldToNew[node]
        
        if node:
            return dfs(node)
        else:
            return None