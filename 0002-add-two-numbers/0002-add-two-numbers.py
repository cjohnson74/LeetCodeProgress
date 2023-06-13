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
        print(num1)
            
        currNode = l2
        while currNode:
            num2.append(currNode.val)
            currNode = currNode.next
        print(num2)
        
        if len(num1) > 0:
            num1.reverse()
            num1str = ''.join([str(num) for num in num1])
        else:
            num1 = '0'
        print(num1str)
        
        print(num1)
        if len(num2) > 0:
            num2.reverse()
            num2str = ''.join([str(num) for num in num2])
        else:
            num2 = '0'
        print(num2str)
        
        sumNums = int(num1str) + int(num2str)
        print(sumNums)
        
        sumArray = []
        for num in str(sumNums):
            sumArray.append(num)
        sumArray.reverse()
        print(sumArray)
        
        dummy = ListNode(0)
        sumNode = ListNode(0)
        dummy = sumNode
        
        for num in sumArray:
            print(num)
            sumNode.next = ListNode(num)
            sumNode = sumNode.next

        currNode = dummy.next
        while currNode:
            print(currNode)
            currNode = currNode.next
        
        return dummy.next