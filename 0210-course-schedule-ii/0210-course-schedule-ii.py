class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = { i:[] for i in range(numCourses) }
        visiting = set()
        
        for course, prereq in prerequisites:
            courses[course].append(prereq)
            
        order = []
        
        for course in courses:
            if courses[course] == []:
                order.append(course)
        
        def dfs(course):
            if course in visiting:
                return False
            
            if courses[course] == []:
                return True
            
            visiting.add(course)
            
            for prereq in courses[course]:
                if (not dfs(prereq)): return False
                
            visiting.remove(course)
            courses[course] = []
            order.append(course)
            return True
        
        for course in range(numCourses):
            if (not dfs(course)): return []
            
        return order