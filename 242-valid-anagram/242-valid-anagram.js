/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if (s.length != t.length) return false;
    
    var sortedS = s.split('').sort().join('');
    var sortedT = t.split('').sort().join('');
    
    for (let i = 0; i < s.length; i++) {
        if (sortedS[i] !== sortedT[i]) return false;
    }

    return true;
};