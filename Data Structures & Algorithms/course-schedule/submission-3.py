from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # logic is, 
        # first build an adjacency dictionary of what goes where
        # go through each course and see if it creates a loop
        # if any course has a loop return False, otherwise return True
        # have two sets, a set of what came already in your path (to see if it comes again) 
        # and a second set to see what paths u've already visited to optimize and bring from O (V*E) worst case to O(V+E) worst case
        # if its in visited, not cycle, if its in path cycle, if u get to end with no issue, not cycle

        path = set()
        visited = set()

        adjacency_dict = defaultdict(list)
        for pair in prerequisites:
            adjacency_dict[pair[0]].append(pair[1])

        def dfs(course):
            if course in visited:
                return False
            if course in path:
                return True
            path.add(course)
            for neighbor in adjacency_dict[course]:
                if dfs(neighbor):
                    return True
            path.discard(course)
            visited.add(course)
            return False

        
        for course in range(numCourses):
            if dfs(course)==True:
                return False
        return True
