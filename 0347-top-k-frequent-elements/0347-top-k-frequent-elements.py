class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # have a freq map O(n) and space
        # array of arrays [-freq, lett] # O(n)
        # heapify array O(n) time and space
        # result = []
        # for i in range(k)
            # result.append(-1 * heapq.heappop(heap))
        # return result
        freqMap = {}
        
        for num in nums:
            if num not in freqMap:
                freqMap[num] = 0
            freqMap[num] += 1
            
        freqMapItems = [[(-1 * freqMap[num]), num] for num in freqMap]
        print(freqMapItems)
        heapq.heapify(freqMapItems)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(freqMapItems)[1])
            
        return res