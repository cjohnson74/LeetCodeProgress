/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    var map = {};
    
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] in map) {
            return [map[nums[i]], i];
        } else {
            let potentialMatch = target - nums[i];
            if (!(potentialMatch in map)) map[potentialMatch] = i;
        }
    }
}; 