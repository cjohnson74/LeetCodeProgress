/**
 * @param {number[][]} grid
 * @return {number}
 */
var orangesRotting = function(grid) {
    var rowMax = grid.length;
    var colMax = grid[0].length;
    var fresh = 0;
    var time = 0;
    var rottenQueue = [];
    
    for (var row = 0; row < rowMax; row++) {
        for (var col = 0; col < colMax; col++) {
            if (grid[row][col] === 1) fresh++;
            if (grid[row][col] === 2) rottenQueue.push([row, col]);
        }
    }
    
    while (rottenQueue.length > 0 && fresh > 0) {
        var rQueLen = rottenQueue.length;
        
        for (let rotten = 0; rotten < rQueLen; rotten++) {
            var [row, col] = rottenQueue.shift();
        
            var indices = [[1,0], [-1,0], [0,1], [0,-1]];
            for (var index of indices) {
                var [rowIndex, colIndex] = index;
                var rowNeighbor = row + rowIndex;
                var colNeighbor = col + colIndex;
                var inbound = rowNeighbor < rowMax && rowNeighbor >= 0 && colNeighbor < colMax && colNeighbor >= 0;
                if (inbound && grid[rowNeighbor][colNeighbor] === 1) {
                    grid[rowNeighbor][colNeighbor] = 2;
                    rottenQueue.push([rowNeighbor, colNeighbor])
                    fresh--;
                }
            }
        }
        time++;   
    }
    
    return fresh > 0 ? -1 : time;
};