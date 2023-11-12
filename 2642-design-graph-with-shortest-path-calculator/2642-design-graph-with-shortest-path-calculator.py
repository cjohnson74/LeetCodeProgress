class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = [[] for _ in range(n)]
        for elm1, elm2, weight in edges:
            self.graph[elm1].append([elm2, weight])

    def addEdge(self, edge: List[int]) -> None:
        elm1, elm2, weight = edge
        self.graph[elm1].append([elm2, weight])

    def shortestPath(self, node1: int, node2: int) -> int:
        queue = []
        queue.append([0, node1])
        distOfElm = {elm: float("inf") for elm in range(len(self.graph))}
        distOfElm[node1] = 0

        while(queue):
            currDist, elm = heapq.heappop(queue)
            if currDist > distOfElm[elm]:
                continue
            if elm == node2:
                return currDist
            for [neighbor, weight] in self.graph[elm]:
                newDist = distOfElm[elm] + weight
                if newDist < distOfElm[neighbor]:
                    distOfElm[neighbor] = newDist
                    heapq.heappush(queue, [newDist, neighbor])
        return -1

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)