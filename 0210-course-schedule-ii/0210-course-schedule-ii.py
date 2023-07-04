class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = { i:[] for i in range(numCourses) }
        
        for course, prereq in prerequisites:
            courses[course].append(prereq)
        
        # a course has 3 possible states:
        # unvisited -> course not added to output or cycle
        # visiting -> course has not been added to output, but added to cycle
        # visited -> course has been added to output
        
        visiting, visited = set(), set()
            
        order = []
        
        def dfs(course):
            if course in visiting:
                return False
            
            if course in visited:
                return True
            
            visiting.add(course)
            
            for prereq in courses[course]:
                if (not dfs(prereq)): return False
                
            visiting.remove(course)
            visited.add(course)
            order.append(course)
            return True
        
        for course in range(numCourses):
            if (not dfs(course)): return []
            
        return order