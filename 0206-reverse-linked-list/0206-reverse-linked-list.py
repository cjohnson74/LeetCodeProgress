# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode = None
        currNode = head
        def revList(currNode, prevNode):
            if currNode == None:
                return prevNode
            temp = currNode.next
            currNode.next = prevNode
            return revList(temp, currNode)
        
        return revList(currNode, prevNode)
            