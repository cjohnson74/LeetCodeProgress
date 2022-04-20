/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    var map = {};
    for(let i = 0; i < nums.length; i++) {
        if (map.hasOwnProperty(nums[i])) {
            map[nums[i]]++;
        } else {
            map[nums[i]] = 1;
        }
    }
    console.log(map);
    console.log(Object.keys(map));
    
    var answer = [];
    for (let key in map) {
        answer.push([key, map[key]]);
    }
    answer.sort((a, b) => b[1] - a[1]);
    return answer.slice(0, k).map((x) => x[0]);
};