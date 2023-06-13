# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = {}
        
        currNode = head
        
        while currNode:
            if (currNode in visited):
                return True
            else:
                visited[currNode] = True
            currNode = currNode.next
            
        return False