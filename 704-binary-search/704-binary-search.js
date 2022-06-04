/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    var leftIdx = 0;
    var rightIdx = nums.length - 1;
    while (leftIdx <= rightIdx) {
        var midIdx = Math.floor((leftIdx+rightIdx)/2);
        var midNum = nums[midIdx];

        if(midNum == target) return midIdx;
        if(midNum < target) {
            leftIdx = midIdx + 1;
        } else {
            rightIdx = midIdx - 1;
        }
    }
    return -1;
};