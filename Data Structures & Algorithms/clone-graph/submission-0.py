"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = {}
        
        def dfs(og):
            if og in visited:
                return visited[og]
            
            cloned = Node(og.val)
            visited[og] = cloned

            for n in og.neighbors:
                cloned.neighbors.append(dfs(n))
            
            return cloned
        
        return dfs(node)