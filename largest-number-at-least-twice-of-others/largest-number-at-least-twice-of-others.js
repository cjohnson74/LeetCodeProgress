/**
 * @param {number[]} nums
 * @return {number}
 */
var dominantIndex = function(nums) {
    var sortedNums = nums.slice().sort((a,b) => a-b);
    var largestNum = sortedNums[sortedNums.length-1];
    console.log(largestNum);
    for(var i = 0; i < sortedNums.length - 1; i++){
        if((sortedNums[i]*2)>largestNum) return -1;
    }
    for(var i = 0; i < nums.length; i++){
        console.log(nums[i]);
        if(nums[i] === largestNum) return i;
    }
};