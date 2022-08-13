/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    var set = {};
    var occerences = {};
    var highestK = 0;
    var result = [];
    
    for (let num of nums) {
        if (!(num in set)) set[num] = 0;
        set[num]++;
    }
    
    for (let key in set) {
        var number = key;
        var occerence = set[key];
        if (occerence > highestK) highestK = occerence;
        if (!(occerence in occerences)) occerences[occerence] = [];
        occerences[occerence].push(number);
    }
    
    while (k > 0) {
        while (occerences[highestK] !== undefined && occerences[highestK].length > 0) {
            result.push(occerences[highestK].pop());
            k--;
        }
        highestK--;
    }
    return result;
};