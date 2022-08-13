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
                currIsland += dfs(grid, row, col, rowMax, colMax, visited);
            }
            largestIsland = Math.max(largestIsland, currIsland);
        }
    }
    
    return largestIsland;
};

var dfs = function(grid, row, col, rowMax, colMax, visited) {
    var rowInbound = row >= 0 && row < rowMax;
    var colInbound = col >= 0 && col < colMax;
    var inbounds = rowInbound && colInbound;
    if (!inbounds) return 0;
    
    if (grid[row][col] === 0) return 0;
    
    var pos = row + ',' + col;
    if (visited.has(pos)) {
        return 0;
    } else {
        visited.add(pos);
    }
    
    var size = 1;
    size += dfs(grid, row-1, col, rowMax, colMax, visited);
    size += dfs(grid, row+1, col, rowMax, colMax, visited);
    size += dfs(grid, row, col-1, rowMax, colMax, visited);
    size += dfs(grid, row, col+1, rowMax, colMax, visited);
    return size;
}