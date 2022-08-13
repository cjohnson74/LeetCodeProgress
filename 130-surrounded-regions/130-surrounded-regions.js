/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solve = function(board) {
    var rowMax = board.length;
    var colMax = board[0].length;
    var notFlippable = new Set();
    
    for (let row = 0; row < rowMax; row++) {
        for (let col = 0; col < colMax; col++) {
            if (row === 0 && board[row][col] === 'O' || col === 0 && board[row][col] === 'O' || row === rowMax-1 && board[row][col] === 'O' || col === colMax-1 && board[row][col] === 'O') {
                dfsMakeUnflippable(board, row, col, rowMax, colMax, notFlippable);
            }
        }
    }
    
    for (let row = 0; row < rowMax; row++) {
        for (let col = 0; col < colMax; col++) {
            var pos = row + ',' + col;
            if(board[row][col] === 'O' && !(notFlippable.has(pos))) flip(board, row, col, rowMax, colMax);
        }
    }
    console.log(board)
    return board;
};

var dfsMakeUnflippable = function(board, row, col, rowMax, colMax, notFlippable) {
    if (board[row][col] === 'X') return;
    
    var pos = row + ',' + col;
    if (notFlippable.has(pos)) return;
    notFlippable.add(pos);
    
    if (row+1 < rowMax) dfsMakeUnflippable(board, row+1, col, rowMax, colMax, notFlippable);
    if (row-1 >= 0) dfsMakeUnflippable(board, row-1, col, rowMax, colMax, notFlippable);
    if (col+1 < colMax) dfsMakeUnflippable(board, row, col+1, rowMax, colMax, notFlippable);
    if (col-1 >= 0) dfsMakeUnflippable(board, row, col-1, rowMax, colMax, notFlippable);
    return;
}

var flip = function(board, row, col, rowMax, colMax) { 
    board[row][col] = 'X';
    
    if (row+1 < rowMax && board[row+1][col] === 'O') flip(board, row+1, col, rowMax, colMax);
    if (row-1 >= 0 && board[row-1][col] === 'O') flip(board, row-1, col, rowMax, colMax);
    if (col+1 < colMax && board[row+1][col] === 'O') flip(board, row, col+1, rowMax, colMax);
    if (col-1 >= 0 && board[row-1][col] === 'O') flip(board, row, col-1, rowMax, colMax);
    return;
}