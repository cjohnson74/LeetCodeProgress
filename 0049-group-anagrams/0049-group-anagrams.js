/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    var anagramGroups = {};
    
    for (let word of strs) {
        var sortedWord = word.split('').sort().join('');
        if (!(sortedWord in anagramGroups)) anagramGroups[sortedWord] = [];
        anagramGroups[sortedWord].push(word);
    }
    
    return Object.values(anagramGroups);
};