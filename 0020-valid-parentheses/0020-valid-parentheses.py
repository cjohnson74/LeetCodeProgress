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
                if stack:
                    poppedBracket = stack.pop()
                    if poppedBracket != brackets[bracket]:
                        return False
                else:
                    return False
            else:
                stack.append(bracket)
                
                
        if stack:
            return False
        return True
            
        
        