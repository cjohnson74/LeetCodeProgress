class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[pos, spd] for pos, spd in zip(position, speed)]
        stack = []
        
        for pos, spd in sorted(cars)[::-1]: # reverse sorted order
            stack.append((target - pos) / spd)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)