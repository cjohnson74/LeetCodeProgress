class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        length = len(nums)
        output = 0
        while length >= k:
            output = heapq.heappop(nums)
            length -= 1
            
        return output