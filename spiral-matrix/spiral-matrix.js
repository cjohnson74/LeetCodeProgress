/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
    var output = [];
    spiralFill(matrix, 0, matrix.length - 1, 0, matrix[0].length - 1, output)
    return output;
};

function spiralFill(matrix, rowStart, rowEnd, colStart, colEnd, output){
    if(rowStart > rowEnd || colStart > colEnd) return;
    
    for(var col = colStart; col <= colEnd; col++){
        output.push(matrix[rowStart][col]);
    }
    for(var row = rowStart + 1; row <= rowEnd; row++){
        output.push(matrix[row][colEnd]);
    }
    for(var col = colEnd - 1; col >= colStart; col--){
        if(rowStart == rowEnd) break;
        output.push(matrix[rowEnd][col]);
    }
    for(var row = rowEnd - 1; row >= rowStart + 1; row--){
        if(colStart == colEnd) break;
        output.push(matrix[row][colStart]);
    }
    spiralFill(matrix, rowStart + 1, rowEnd - 1, colStart + 1, colEnd - 1, output)
    
}