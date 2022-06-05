/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    k %= nums.length;
    
    const reverse = (leftIdx, rightIdx) => {
        while(leftIdx < rightIdx){
            var temp = nums[leftIdx];
            nums[leftIdx] = nums[rightIdx];
            nums[rightIdx] = temp;
            leftIdx++;
            rightIdx--;
        }
    }
    reverse(0, nums.length-1);
    reverse(0, k-1);
    reverse(k, nums.length-1);
};