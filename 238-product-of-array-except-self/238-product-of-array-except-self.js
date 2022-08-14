/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    var result = Array(nums.length).fill(1);
    
    var product = 1
    for (let i = 0; i <= nums.length-1; i++) {
        result[i] *= product;
        product *= nums[i];
    }
    
    var product = 1;
    for (let i = nums.length-1; i >= 0; i--) {
        result[i] *= product;
        product *= nums[i];
    }
    
    return result;
};