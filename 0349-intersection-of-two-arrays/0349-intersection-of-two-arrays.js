/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function(nums1, nums2) {
    var intersections = new Set();
    var visited = {};
    
    for (let num of nums1) {
        if (!(num in visited)) {
            visited[num] = true;
        }
    }
    
    for (let num of nums2) {
        if (num in visited) {
            intersections.add(num);
        }
    }
    
    return [...intersections]
};