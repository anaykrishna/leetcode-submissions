class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan(a, b):
            return abs(points[a][0] - points[b][0]) + abs(points[a][1] - points[b][1])

        n = len(points)
        visited = [False] * n
        dist = [float('inf')] * n
        dist[0] = 0     
        ans = 0

        for _ in range(n):
            u = min((i for i in range(n) if not visited[i]), key=lambda i : dist[i])
            visited[u] = True
            ans += dist[u]

            for v in range(n):
                if not visited[v]:
                    dist[v] = min(dist[v], manhattan(u, v))
        
        return ans




        
