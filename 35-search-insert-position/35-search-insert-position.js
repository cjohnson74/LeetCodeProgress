/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    let left = 0;
    let right = nums.length - 1;
    
    do {
        const i = Math.floor((right - left) / 2) + left;
        
        const value = nums[i];
        
        if (value > target) {
            right = i - 1;
        } else if (value < target) {
            left = i + 1;
        } else {
            return i;
        }
        
    } while (right - left >= 0);
    
    return left;
};