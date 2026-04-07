class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        parent = [i for i in range(n)]

        def find(node):
            if parent[node] == node:
                return node
            return find(parent[node])
        
        def union(x, y):
            f1, f2 = find(x), find(y) 
            if f1 == f2:
                return False
            else:
                parent[f2] = f1
                return True
        
        ans = []
        for u, v in edges:
            if not union(u, v):
                ans = [u, v]
        
        return ans