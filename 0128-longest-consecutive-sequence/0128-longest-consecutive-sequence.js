/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    var numsSet = new Set(nums);
    var longestStreak = 0;
    
    for (num of numsSet) {
        if (!(numsSet.has(num-1))) {
            currNum = num;
            currStreak = 1;
            
            while (numsSet.has(currNum+1)) {
                currNum++;
                currStreak++;
            }
            
            longestStreak = Math.max(currStreak, longestStreak);
        }
    }
    
    return longestStreak;
};