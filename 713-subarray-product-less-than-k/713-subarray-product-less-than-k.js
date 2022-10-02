/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var numSubarrayProductLessThanK = function(nums, k) {
    var currProd = 1;
    var subCount = 0;
    var start = 0;
    
    for (let end = 0; end < nums.length; end++) {
        currProd *= nums[end];
        while (currProd >= k && start <= end) {
            currProd /= nums[start++];
        }
        
        subCount += end - start + 1;
    }
    
    return subCount;
};