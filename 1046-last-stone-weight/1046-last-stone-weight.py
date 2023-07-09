class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # max heapify stones using -weight
        # while len(stones) > 1
        # biggestStone = pop heap
        # secondBiggestStone = pop heap
        # if biggestStone != secondBiggestStone
            # push onto heap biggestStone - secondBiggestStone
            
        # return stones[0]
        for i in range(len(stones)):
            stones[i] = stones[i] * -1
        
        heapq.heapify(stones)
        
        while len(stones) > 1:
            biggestStone = heapq.heappop(stones) * -1
            secondBiggestStone = heapq.heappop(stones) * -1
            
            if biggestStone != secondBiggestStone:
                heapq.heappush(stones, (biggestStone - secondBiggestStone) * -1)
                
        return stones[0] * -1 if stones else 0