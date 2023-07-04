class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create a graph out of the adjacency list
        
        # check for cycles by keeping a visited set
            # black
            # white
            # gray
        
        # when visiting a node it is gray
        # when all neighbors have been visited the class is white
        # when something is not visited it is black
        courses = {}
        for course, prereq in prerequisites:
            if course not in courses:
                courses[course] = []
            courses[course].append(prereq)
            if prereq not in courses:
                courses[prereq] = []
                
        visiting = set()
        
        def dfs(course):
            if course in visiting:
                return False
            
            if len(courses[course]) == 0:
                return True
            
            visiting.add(course)

            for neighbor in courses[course]:
                if (dfs(neighbor)):
                    courses[course].remove(neighbor)
                else:
                    return False

            visiting.remove(course)
            return True
        
        if len(prerequisites) == 0:
            return True

        for course in courses:
            if len(courses[course]) != 0:
                if (not dfs(course)):
                    return False
                
        return True
            
            
            
            
                
            