/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    var rowMax = grid.length;
    var colMax = grid[0].length;
    var count = 0;
    var visited = new Set();
    
    for (let row = 0; row < rowMax; row++) {
        for (let col = 0; col < colMax; col++) {
            if (grid[row][col] === '1') {
                count += dfs(grid, row, col, rowMax, colMax,visited);
            }
        }
    }
    
    return count++;
};

var dfs = function(grid, row, col, rowMax, colMax, visited) {
    if (grid[row][col] === '0') return 0;
    
    var pos = row + ',' + col;
    if (visited.has(pos)) return 0;
    visited.add(pos);
    
    if (row-1 >= 0) dfs(grid, row-1, col, rowMax, colMax, visited);
    if (row+1 < rowMax) dfs(grid, row+1, col, rowMax, colMax, visited);
    if (col-1 >= 0) dfs(grid, row, col-1, rowMax, colMax, visited);
    if (col+1 < colMax) dfs(grid, row, col+1, rowMax, colMax, visited);
    return 1;
}