class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        graph = defaultdict(list)
        UNVISITED = 0
        VISITING = 1 
        VISITED = 2

        states = [0] * numCourses

        for a,b in prerequisites:
            graph[a].append(b)
        

        def dfs(node):
            state = states[node]

            if state == VISITING:
                return False
            elif state == VISITED:
                return True

            states[node] = VISITING

            for nei in graph[node]:
                if not dfs(nei):
                    return False
            
            states[node] = VISITED
            order.append(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return order
            
