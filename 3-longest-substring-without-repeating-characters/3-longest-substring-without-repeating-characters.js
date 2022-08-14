/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    var map = {};
    var pointer = 0;
    var max = 0;
    var length = s.length;
    
    for (let i = 0; i < length; i++) {
        var char = s[i];
        
        if (map[char] !== undefined) {
            pointer = Math.max(map[char], pointer);
        }
        max = Math.max(max, i - pointer + 1);
        map[char] = i + 1;
    }
    
    return max;
};