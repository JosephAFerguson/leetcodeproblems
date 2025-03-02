class Solution:
    def traverse(self,i, isConnected: List[List[int]], visited) -> int:
        n = len(isConnected)
        visited[i] = 1
        for col in range(n):
            # only visit those that are connected(obviously) and those cities not visited
            if isConnected[col][i] and not visited[col]:
                self.traverse(col, isConnected, visited)
                    
        
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        Notes: DFS/BFS search obviously
                Start with a city, travel to each and every city it is connected too, marking them visited on the array,
                    when traversal is done, add 1 to the result provinces
                Rinse and repeat with unvisited provinces
             - To be faster you can mark rows as visited, less checking on the root function, makes it more like 0(n)
        """
        n = len(isConnected) 
        visited = [0]*n
        res = 0
         
        for i in range(n):
            if not (visited[i]):
                self.traverse(i,isConnected, visited)
                res+=1
        return res
