/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function(nums) {
    var totalSum = 0;
    var n = nums.length;
    var leftSum = 0;
    if(nums.length === 0) return -1;
    for(var num of nums){
        totalSum += num;
    }
    for(var i = 0; i < n; i++){
        if(leftSum == (totalSum - nums[i])) {
            return i;
        } else {
            leftSum += nums[i];
            totalSum -= nums[i];
        }
        
    }
    return -1;
    
};