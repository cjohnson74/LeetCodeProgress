/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    var leftIdx = 0;
    var rightIdx = nums.length - 1;
    var midIdx;
    if(nums[rightIdx] < target) {
        return rightIdx + 1;;
    }
    if(nums[leftIdx] > target) {
        return leftIdx;
    }
    while(leftIdx <= rightIdx){
        var midIdx = Math.floor((leftIdx + rightIdx) / 2);
        var midNum = nums[midIdx];
        
        if(midNum == target){
            return midIdx;
        } else if (midNum > target && nums[midIdx-1] < target) {
            return midIdx;
        }
        
        if(midNum < target){
            leftIdx = midIdx + 1;
        } else {
            rightIdx = midIdx - 1;
        }
    }
    return midIdx;
};