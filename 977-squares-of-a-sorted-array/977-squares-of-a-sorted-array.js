/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
    var squaredNums = [];
    var leftPointer = 0;
    var rightPointer = nums.length - 1;
    while(leftPointer <= rightPointer){
        var leftNum = Math.abs(nums[leftPointer]);
        var rightNum = Math.abs(nums[rightPointer]);
        if(leftNum > rightNum) {
            squaredNums.push(leftNum*leftNum);
            leftPointer++;
        } else {
            squaredNums.push(rightNum*rightNum);
            rightPointer--;
        }
    }
    return squaredNums.sort((a,b) => a-b);
};