/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const brackets = {
        '{':'}',
        '(':')',
        '[':']'
    }
    var stack = [];
    for (let bracket of s.split('')) {
        if (bracket in brackets) {
            stack.push(bracket);
        } else {
            if (brackets[stack.pop()] != bracket) {
                return false;
            }
        }
    }
    if (stack.length > 0) return false;
    return true;
};