/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    console.log(s.split(' '))
    return s.split(' ').map((word) => word.split('').reverse().join('')).join(' ')
};