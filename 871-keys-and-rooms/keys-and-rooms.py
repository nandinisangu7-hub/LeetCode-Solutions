class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=[False]*len(rooms)
        visited[0]=True
        d=deque([0])
        while d:
            room=d.popleft()
            for key in rooms[room]:
                if not visited[key]:
                    visited[key]=True
                    d.append(key)
        return all(visited)
        