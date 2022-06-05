/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const map = new Map();
    
    for(var i = 0; i < nums.length; i++) {
        var possMatch = target - nums[i];
        if(map.hasOwnProperty(nums[i])) {
            return [ map[nums[i]] , i];
        }
        map[possMatch] = i;
    }
    return [];
};