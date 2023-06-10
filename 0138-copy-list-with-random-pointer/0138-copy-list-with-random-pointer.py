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
        
        nodes = {}
        newNodes = {}
        
        # iterate through linkedlist
        # create new node
        # check if random is visited
            #if random is created in copy
                # make random point to node in copy
            # else
                # make random point to new node
        # make next point to new next node
        # make next currNodeCopy
        
        nodeKey = 0
        currNode = head
        
        while currNode:
            nodes[currNode] = nodeKey
            nodeKey += 1
            currNode = currNode.next
        nodes[nodeKey] = None
        
        currNode = head
        currNodeCopy = Node(currNode.val)
        dummy.next = currNodeCopy
        
        while currNode:
            nodeKey = nodes[currNode]
            if nodeKey not in newNodes:
                newNodes[nodeKey] = None
            newNodes[nodeKey] = currNodeCopy
            currNodeCopy.val = currNode.val
            if currNode.next == None:
                currNodeCopy.next = None
            else:
                nextNodeKey = nodes[currNode.next]
                if nextNodeKey not in newNodes:
                    newNodes[nextNodeKey] = Node(currNode.next.val)
                    currNodeCopy.next = newNodes[nextNodeKey]
                else:
                    currNodeCopy.next = newNodes[nextNodeKey]
            
            if currNode.random == None:
                currNodeCopy.random = None
            else:
                randomNodeKey = nodes[currNode.random]
                if randomNodeKey not in newNodes:
                    newNodes[randomNodeKey] = Node(currNode.random.val)
                    currNodeCopy.random = newNodes[randomNodeKey]
                else:
                    currNodeCopy.random = newNodes[randomNodeKey]
            currNode = currNode.next
            currNodeCopy = currNodeCopy.next
        
        return dummy.next
        