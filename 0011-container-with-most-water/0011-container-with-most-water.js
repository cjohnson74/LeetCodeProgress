/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    var leftPointer = 0;
    var rightPointer = height.length-1;
    var maxVolume = 0;
    
    while (leftPointer < rightPointer) {
        var currVolume = 0;
        if (height[leftPointer] > height[rightPointer]) {
            currVolume = height[rightPointer] * (rightPointer-leftPointer);
            rightPointer--;
        } else {
            currVolume = height[leftPointer] * (rightPointer-leftPointer);
            leftPointer++;
        }
        maxVolume = Math.max(currVolume, maxVolume);
    }
    
    return maxVolume;
};