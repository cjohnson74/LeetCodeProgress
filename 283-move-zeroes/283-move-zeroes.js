/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    var lastNonZeroIndex = 0;
    for(var i = 0; i < nums.length; i++){
        if(nums[i] != 0){
            nums[lastNonZeroIndex++] = nums[i];
        }
    }
    
    for(var i = lastNonZeroIndex; i < nums.length; i++){
        nums[i] = 0;
    }
};