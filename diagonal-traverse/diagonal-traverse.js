/**
 * @param {number[][]} mat
 * @return {number[]}
 */
var findDiagonalOrder = function(mat) {
    var holder = {};
    for(var row = 0; row < mat.length; row++){
        for(var col = 0; col < mat[row].length; col++){
            if(!holder.hasOwnProperty((row+col))){
                holder[row+col] = [mat[row][col]];
            } else {
                holder[row+col].push(mat[row][col]);
            }
        }
    }
    var output = [];
    for(var entry of Object.entries(holder)){
        if(entry[0] % 2 == 0){
            for(var i = entry[1].length - 1; i >= 0; i--){
                output.push(entry[1][i]);
            }
        } else {
            for(var x of entry[1]){
                output.push(x);
            }
        }
    }
    return output;
};