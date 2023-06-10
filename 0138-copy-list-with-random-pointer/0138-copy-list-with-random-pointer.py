"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        dummy = Node(0)
        
        oldToNew = {None: None}
        
        # iterate through linkedlist
        # create new node
        # check if random is visited
            #if random is created in copy
                # make random point to node in copy
            # else
                # make random point to new node
        # make next point to new next node
        # make next currNodeCopy
        
        currNode = head
        
        while currNode:
            copy = Node(currNode.val)
            oldToNew[currNode] = copy
            currNode = currNode.next
        
        currNode = head
        dummy.next = oldToNew[currNode]
        
        while currNode:
            copy = oldToNew[currNode]
            copy.random = oldToNew[currNode.random]
            copy.next = oldToNew[currNode.next]
            currNode = currNode.next
        
        return dummy.next
        