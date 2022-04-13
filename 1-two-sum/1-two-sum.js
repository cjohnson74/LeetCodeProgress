/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const map = {}
    
    for(let i = 0; i < nums.length; i++){
        var goal = target - nums[i];
        if(map.hasOwnProperty(nums[i])){
            return ([nums.indexOf(goal), i])
        }
        map[goal] = i
    }
};