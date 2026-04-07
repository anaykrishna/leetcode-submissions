class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[v].append(u)

        visited = [0] * numCourses
        ans = []

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
            ans.append(node)
            return True
        
        for i in range(numCourses):
            if visited[i] == 0:
                b1 = dfs(i)
                if not b1:
                    return []
        
        return ans[::-1]
