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
        counts = [[] for i in range(len(nums) + 1)]
        
        for num in nums:
            freqMap[num] = 1 + freqMap.get(num, 0)
            
        for num, freq in freqMap.items():
            counts[freq].append(num)
        
        res = []
        for i in range(len(counts) - 1, 0, -1):
            for num in counts[i]:
                res.append(num)
            if len(res) == k:
                return res