class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create a graph out of the adjacency list
        
        # have a visiting set to detect cycles
        
        # remove the course from the prereq list
        
        # if the prereq list is empty they we can return true in dfs
        
        # if the course is in visiting set we can return fails because a cycle was detected
        
        courses = {}
        visiting = set()
        
        for course, prereq in prerequisites:
            if course not in courses:
                courses[course] = []
            courses[course].append(prereq)
            if prereq not in courses:
                courses[prereq] = []
        
        def dfs(course):
            if course in visiting:
                return False
            
            if courses[course] == []:
                return True
            
            visiting.add(course)

            for prereq in courses[course]:
                if not dfs(prereq): return False

            visiting.remove(course)
            courses[course] = []
            return True
        
        if len(prerequisites) == 0:
            return True

        for course in courses:
            if len(courses[course]) != 0:
                if (not dfs(course)):
                    return False
                
        return True
