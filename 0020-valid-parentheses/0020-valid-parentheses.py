class Solution:
    def isValid(self, s: str) -> bool:
        # if open add to stack
        # if closing pop from stack and compare
            # if not equal return False
        stack = collections.deque()
        brackets = {')': '(',
                    '}': '{',
                    ']': '['
                   }
        
        for bracket in s:
            if bracket in brackets:
                if stack and stack[-1] == brackets[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
                
        return True if not stack else False
            
        
        