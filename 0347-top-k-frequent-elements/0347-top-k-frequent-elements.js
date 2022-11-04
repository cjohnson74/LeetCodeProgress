/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    // create freq map by iterating through nums: key = num, value = freq
    // sort keys of freq map by highest value
        // Object.keys(freq).sort((freq[a],freq[b])=>freq[a]-freq[b]);
    // return first k elements of freq map keys array
    
    var freq = {};
    
    for (let num of nums) {
        if (!(num in freq)) freq[num] = 0;
        freq[num]++;
    }
    
    var sortedKeys = Object.keys(freq).sort((a,b)=>freq[b]-freq[a]);
    console.log(sortedKeys)
    return sortedKeys.slice(0,k);
};