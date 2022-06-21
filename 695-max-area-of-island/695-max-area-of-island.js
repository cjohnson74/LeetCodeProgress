/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxAreaOfIsland = function(grid) {
    const explore = (grid, row, col) => {
    var rowInBounds = 0 <= row && grid.length > row;
    var colInBounds = 0 <= col && grid[0].length > col;
    if(!rowInBounds || !colInBounds) return false;
  
    if(grid[row][col] == 0) return false;
    grid[row][col] = 0;
    currentCount += 1;
  
    explore(grid, row-1, col, currentCount);
    explore(grid, row+1, col, currentCount);
    explore(grid, row, col+1, currentCount);
    explore(grid, row, col-1, currentCount);
    return currentCount;
  }
  var maximumCount = Number.MIN_VALUE;
  var currentCount = 0;
  for(var row = 0; row < grid.length; row++){
    for(var col = 0; col < grid[0].length; col++){
      currentCount = 0;
      currentCount = explore(grid, row, col, currentCount);
      if(currentCount != false){
        maximumCount = Math.max(currentCount, maximumCount);
      }
    }
  }
  return maximumCount;
};