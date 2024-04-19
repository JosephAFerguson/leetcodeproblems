class Solution {
public:
    bool isIn(int i,int j, int iB, int jB){
        return (i <=iB && i>= 0 && j <=jB && j >=0);
    }
    void chain(int i, int j, int iB, int jB, vector<vector<char>>& grid){
        if (!(isIn(i,j,iB,jB))){
            return;
        }else if (grid[i][j] == '0'){
            return;
        }else if (grid[i][j] == '1'){
            grid[i][j] = '0';
            chain(i+1,j,iB,jB, grid);
            chain(i-1,j,iB,jB, grid);
            chain(i,j+1,iB,jB, grid);
            chain(i,j-1,iB,jB, grid);
        }
    }
    int numIslands(vector<vector<char>>& grid) {
        int iB = grid.size()-1;
        int jB = grid[0].size()-1;
        int res = 0;
        for(int i = 0;i <= iB;i++){
            for(int j = 0; j <= jB;j++){
                if(grid[i][j] == '1'){
                    res++;
                    chain(i,j,iB,jB,grid);
                }
            }
        }
        return res;
    }
};
