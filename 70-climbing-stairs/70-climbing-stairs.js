/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n, memo = {}) {
    if (n in memo) return memo[n];
    if (n == 0) return 1;
    if (n < 0) return 0;
    
    var numOfPaths = 0;
    numOfPaths += climbStairs(n-1, memo);
    numOfPaths += climbStairs(n-2, memo);
    memo[n] = numOfPaths;
    return numOfPaths;
};