class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:    
        adj = defaultdict(list)
        visited = set()

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node, parent):
            visited.add(node)

            for nei in adj[node]:
                if nei == parent:
                    continue
                if nei not in visited:
                    dfs(nei, node)

        ans = 0
        for i in range(n):
            if i not in visited:
                dfs(i, -1)
                ans += 1
        
        return ans