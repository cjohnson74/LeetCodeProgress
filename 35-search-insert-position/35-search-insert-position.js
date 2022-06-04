/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    var leftIdx = 0;
    var rightIdx = nums.length - 1;
    var midIdx;
    while(rightIdx - leftIdx >= 0){
        var midIdx = Math.floor((leftIdx + rightIdx) / 2);
        var midNum = nums[midIdx];
        
        if(midNum > target){
            rightIdx = midIdx - 1;
        } else if(midNum < target){
            leftIdx = midIdx + 1;
        } else {
            return midIdx;
        }
    }
    return leftIdx;
};