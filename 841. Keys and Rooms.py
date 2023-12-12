class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        def visit(key):
            keys = rooms[key]
            for i,val in enumerate(keys):
                if val == -1:
                    break
                else: 
                    rooms[key][i]= -1
                    visited.add(key)
                    visit(val)
            visited.add(key)
        visit(0)
        return len(visited) == len(rooms)
