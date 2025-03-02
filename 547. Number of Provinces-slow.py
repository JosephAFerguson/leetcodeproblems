class Solution:
    def traverse(self, row, isConnected: List[List[int]]) -> int:
        n = len(isConnected)    
        for col in range(n):
            if isConnected[row][col]:
                #mark as visited
                isConnected[row][col] = 0
                self.traverse(col, isConnected)
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        Notes: DFS/BFS search obviously
                Start with a city, travel to each and every city it is connected too, marking them visited on the array,
                    when traversal is done, add 1 to the result provinces
                Rinse and repeat with unvisited provinces
        """
        res = 0
        n = len(isConnected)  
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    self.traverse(j, isConnected)
                    res +=1
        return res
