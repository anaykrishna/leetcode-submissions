class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[v].append(u)
        
        visited = [0] * numCourses

        def dfs(node):
            if visited[node] == 1:
                return False
            if visited[node] == 2:
                return True

            visited[node] = 1

            for nei in adj[node]:
                if not dfs(nei):
                    return False
            
            visited[node] = 2
            return True
        
        for u in range(numCourses):
            if not dfs(u):
                return False
        
        return True