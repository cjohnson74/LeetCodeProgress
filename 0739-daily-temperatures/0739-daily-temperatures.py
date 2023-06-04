class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        stack = [] # pair: [idx, temp]
        
        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                popTemp, popIdx = stack.pop()
                res[popIdx] = idx - popIdx
            stack.append([temp, idx])
        return res