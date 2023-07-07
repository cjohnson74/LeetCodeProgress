class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqMap = {task: 0 for task in tasks}
        for task in tasks:
            freqMap[task] += 1
            
        maxHeap = [-freq for freq in freqMap.values()]
        
        heapq.heapify(maxHeap)
        
        queue = deque() # pairs of [-freq, idleTime]
        
        time = 0
        
        while queue or maxHeap:
            time += 1
            if maxHeap:
                freq = heapq.heappop(maxHeap) + 1
                if freq != 0:
                    queue.append([freq, n + time])
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])
            
        return time
        