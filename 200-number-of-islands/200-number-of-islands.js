/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    let noOfIslands = 0;
    
    let m = grid.length;
    let n = grid[0].length;
    
    for(let i = 0; i < m; i++) {
        for(let j = 0; j < n; j++) {
            if(isIsland(grid, i, j)) noOfIslands++;
        }
    }
    
    function isIsland(grid, i, j) {
        if(i < 0 || j < 0 || i >= m || j >= n || grid[i][j] === "0") return false;
        
        grid[i][j] = "0";
        
        isIsland(grid, i + 1, j);
        isIsland(grid, i - 1, j);
        isIsland(grid, i, j + 1);
        isIsland(grid, i, j - 1);
        
        return true;
    }
    return noOfIslands;
};