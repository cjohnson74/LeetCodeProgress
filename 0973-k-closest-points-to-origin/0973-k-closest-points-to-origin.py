class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        output = []
        
        for x, y in points:
            distance = (x*x) + (y*y)
            distances.append([distance, x, y])
            
        heapq.heapify(distances)
        
        while k > 0:
            [distance, x, y] = heapq.heappop(distances)
            output.append([x,y])
            k -= 1
        
        return output