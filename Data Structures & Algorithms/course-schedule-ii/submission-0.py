from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacency_list = defaultdict(list)
        for pair in prerequisites:
            adjacency_list[pair[0]].append(pair[1])
        
        path = set()
        visited = set()
        result = []

        def check_loop(course):
            if course in path:
                return True
            if course in visited:
                return False
            path.add(course)
            for neighbor in adjacency_list[course]:
                if check_loop(neighbor) == True:
                    return True
            path.discard(course)
            visited.add(course)
            result.append(course)

        
        for course in range(numCourses):
            if check_loop(course):
                return []
        
        return result