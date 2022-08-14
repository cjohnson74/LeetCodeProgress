/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    var sums = {};
    
    for (let i = 0; i < nums.length; i++) {
        var possible = target - nums[i];
        if (possible in sums) return [i, nums.indexOf(possible)];
        sums[nums[i]] = i;
    }
};