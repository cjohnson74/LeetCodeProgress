/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    var set = {};
    var result = []
    
    for (let i = 0; i < strs.length; i++) {
        const formate = strs[i].split('').sort().join('');
        
        if (formate in set) {
            set[formate].push(strs[i]);
        } else {
            set[formate] = [strs[i]];
        }
    }
    
    for (let key in set) {
        result.push(set[key]);
    }
    
    return result;
};