# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        leftPnt = head
        rightPnt = head
        currIdx = 0
        while currIdx != n:
            rightPnt = rightPnt.next
            currIdx += 1
        
        prevNode = None
        while rightPnt:
            prevNode = leftPnt
            leftPnt = leftPnt.next
            rightPnt = rightPnt.next
        
        if prevNode:
            prevNode.next = leftPnt.next
            return head
        else:
            return leftPnt.next