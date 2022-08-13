/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    var results = Array(nums.length).fill(1);
    
    var product = 1;
    for (let i = 0; i < nums.length-1; i++) {
        product *= nums[i];
        results[i+1] *= product;
    }
    
    var product = 1;
    for (let i = nums.length-1; i > 0; i--) {
        product *= nums[i];
        results[i-1] *= product
    }
    
    return results
};