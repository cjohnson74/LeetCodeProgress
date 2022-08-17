/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    if (nums.length == 0 || nums == null) return 0;
    
    var set = new Set(nums);
    var longest = -Infinity;
    
    for (let num of set) {
        if (set.has(num-1)) continue;
        
        let currNum = num;
        let currStreak = 1;
        
        while(set.has(currNum+1)) {
            currNum++;
            currStreak++;
        }
        longest = Math.max(currStreak, longest);
    }
    
    return longest;
};