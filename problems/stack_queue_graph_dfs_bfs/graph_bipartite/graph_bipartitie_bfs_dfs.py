## BFS

from collections import deque
from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n  # -1 = not colored, 0 / 1 = two groups
        
        for start in range(n):
            if color[start] != -1:
                continue  # already visited
            
            queue = deque([start])
            color[start] = 0  # color first node
            
            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    # if not colored, paint opposite color
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    # if already colored and same as neighbor -> conflict
                    elif color[v] == color[u]:
                        return False
        
        return True


## DFS


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n
        
        def dfs(u, c):
            color[u] = c
            for v in graph[u]:
                if color[v] == -1:
                    if not dfs(v, 1 - c):
                        return False
                elif color[v] == color[u]:
                    return False
            return True
        
        for i in range(n):
            if color[i] == -1:
                if not dfs(i, 0):
                    return False
        
        return True
