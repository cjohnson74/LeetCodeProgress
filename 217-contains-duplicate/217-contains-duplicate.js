/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    var set = new Set();
    
    for (let num of nums) {
        if (num in set) return true;
        set[num] = true;
    }
    
    return false;
};