/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    var result = [];
    var pointer = 0;
    while (pointer < nums.length){
        var sum = 1;
        for (let i = 0; i < nums.length; i++) {
            if (i !== pointer) sum = sum * nums[i];
        }
        result.push(sum);
        pointer++;
    }
    
    return result;
};