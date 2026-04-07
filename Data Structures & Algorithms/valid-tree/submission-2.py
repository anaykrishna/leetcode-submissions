from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
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
                elif nei in visited:
                    return False
        
                if not dfs(nei, node):
                    return False
            
            return True
       
        b1 = dfs(0, -1)
        b2 = len(visited) == n 

        return b1 and b2