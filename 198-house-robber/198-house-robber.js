/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    var rob1 = 0;
    var rob2 = 0;
    
    for (let num of nums) {
        var temp = Math.max(num + rob1, rob2);
        rob1 = rob2;
        rob2 = temp;
    }
    
    return rob2
};