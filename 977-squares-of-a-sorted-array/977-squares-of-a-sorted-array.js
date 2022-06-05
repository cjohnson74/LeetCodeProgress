/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
    var squaredNums = [];
    var leftPointer = 0;
    var rightPointer = nums.length - 1;
    while(leftPointer <= rightPointer){
        var leftNumSquared = Math.pow(nums[leftPointer],2);
        var rightNumSquared = Math.pow(nums[rightPointer],2);
        if(leftNumSquared > rightNumSquared) {
            squaredNums.push(leftNumSquared);
            leftPointer++;
        } else {
            squaredNums.push(rightNumSquared);
            rightPointer--;
        }
    }
    return squaredNums.sort((a,b) => a-b);
};