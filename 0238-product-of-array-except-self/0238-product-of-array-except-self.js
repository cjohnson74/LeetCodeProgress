/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    // initialize a products array: same length of nums, fill with 1s
    // iterate through nums using for loop increasing idx by 1 starting from 0 ending at nums.length-1
    // for each idx products[i] *= nums[i]
    // iterate through nums using for loop decreading idx by 1 starting from nums.length-1 ending at 0
    // for each idx products[i] *= nums[i];
    
    // the first loop gets all the products of the elements before the idx
    // the second loop gets the product of all the elements after the idx
    var left = new Array(nums.length).fill(1);
    var right = new Array(nums.length).fill(1);
    var answer = [];
    
    var products = new Array(nums.length).fill(1);
    console.log(products)
    for (let i = 1; i < nums.length; i++) {
        left[i] = left[i-1] * nums[i-1];
    }
    console.log(left)
    
    for (let i = nums.length-2; i >= 0; i--) {
        right[i] = right[i+1] * nums[i+1];
    }
    console.log(right)
    
    for (let i = 0; i < nums.length; i++) {
        answer.push(left[i] * right[i]);
    }
    
    return answer;
};