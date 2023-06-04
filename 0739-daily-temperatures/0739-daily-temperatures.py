class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        stack = [] # pair: [temp, idx]
        
        for idx, temp in enumerate(temperatures):
            if len(temperatures) == 0:
                stack.append([temp, i])
                continue
            while len(stack) > 0:
                if stack[-1][0] < temp:
                    popTemp, popIdx = stack.pop()
                    res[popIdx] = idx - popIdx
                else:
                    break
            stack.append([temp, idx])
            
        return res