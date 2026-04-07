class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = [0] * n

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, parent):
            if visited[node] == 1:
                return False
            
            visited[node] = 1
            for neighbor in graph[node]:
                if parent == neighbor:
                    continue
                if not dfs(neighbor, node):
                    return False
            
            return True
                
        
        if not dfs(0, -1):
            return False
        
        return all(visited)
