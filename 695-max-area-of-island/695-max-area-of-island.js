/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxAreaOfIsland = function(grid) {
    var rowMax = grid.length;
    var colMax = grid[0].length;
    var largestIsland = -Infinity;
    var visited = new Set();
    
    
    for (let row = 0; row < rowMax; row++) {
        for (let col = 0; col < colMax; col++) {
            var currIsland = 0;
            if (grid[row][col] === 1) {
                currIsland += dfs(grid, row, col, rowMax, colMax);
            }
            largestIsland = Math.max(largestIsland, currIsland);
        }
    }
    
    return largestIsland;
};

var dfs = function(grid, row, col, rowMax, colMax) {
    var rowInbound = row >= 0 && row < rowMax;
    var colInbound = col >= 0 && col < colMax;
    var inbounds = rowInbound && colInbound;
    if (!inbounds) return 0;
    
    if (grid[row][col] === 0) return 0;
    
    grid[row][col] = 0;
    
    var size = 1;
    size += dfs(grid, row-1, col, rowMax, colMax);
    size += dfs(grid, row+1, col, rowMax, colMax);
    size += dfs(grid, row, col-1, rowMax, colMax);
    size += dfs(grid, row, col+1, rowMax, colMax);
    return size;
}