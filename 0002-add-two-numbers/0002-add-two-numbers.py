# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        currNode = l1
        num1 = []
        num2 = []
        
        while currNode:
            num1.append(currNode.val)
            currNode = currNode.next
            
        currNode = l2
        while currNode:
            num2.append(currNode.val)
            currNode = currNode.next
        
        if len(num1) > 0:
            num1.reverse()
            num1str = ''.join([str(num) for num in num1])
        else:
            num1 = '0'
        
        if len(num2) > 0:
            num2.reverse()
            num2str = ''.join([str(num) for num in num2])
        else:
            num2 = '0'
        
        sumNums = int(num1str) + int(num2str)
        
        sumArray = []
        for num in str(sumNums):
            sumArray.append(num)
        sumArray.reverse()
        
        dummy = ListNode(0)
        sumNode = ListNode(0)
        dummy = sumNode
        
        for num in sumArray:
            sumNode.next = ListNode(num)
            sumNode = sumNode.next
        
        return dummy.next