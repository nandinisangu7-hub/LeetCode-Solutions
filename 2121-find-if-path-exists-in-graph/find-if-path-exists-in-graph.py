class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited=[False]*n
        visited[source]=True
        d=deque([source])
        ans=[]
        while d:
            ele=d.popleft()
            if ele==destination:
                return True
            for nei in graph[ele]:
                if not visited[nei]:
                    d.append(nei)
                    visited[nei]=True
        return False


        