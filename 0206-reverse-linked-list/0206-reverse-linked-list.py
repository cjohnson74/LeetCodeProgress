# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode, currNode = None, head
        # T O(n), M O(n)
        def revList(currNode, prevNode):
            if currNode == None:
                return prevNode
            nxt = currNode.next
            currNode.next = prevNode
            return revList(nxt, currNode)
        
        return revList(currNode, prevNode)
            