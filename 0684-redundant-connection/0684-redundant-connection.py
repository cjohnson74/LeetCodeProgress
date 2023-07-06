class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {}
        
        def dfs(node, target):
            if node not in visited:
                visited.add(node)
                if node == target: return True
                for neighbor in graph[node]:
                    if dfs(neighbor, target): return True
                
        for node, neighbor in edges:
            visited = set()
            if node in graph and neighbor in graph and dfs(node, neighbor):
                return node, neighbor
            if node not in graph:
                graph[node] = set()
            if neighbor not in graph:
                graph[neighbor] = set()
            graph[node].add(neighbor)
            graph[neighbor].add(node)