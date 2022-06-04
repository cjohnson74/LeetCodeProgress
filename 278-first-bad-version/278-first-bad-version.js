/**
 * Definition for isBadVersion()
 * 
 * @param {integer} version number
 * @return {boolean} whether the version is bad
 * isBadVersion = function(version) {
 *     ...
 * };
 */

/**
 * @param {function} isBadVersion()
 * @return {function}
 */
var solution = function(isBadVersion) {
    /**
     * @param {integer} n Total versions
     * @return {integer} The first bad version
     */
    return function(n) {
        var leftVersion = 0;
        var rightVersion = n;
        var midVersion;
        while (leftVersion <= rightVersion) {
            midVersion = Math.floor((leftVersion + rightVersion) / 2)
            if(isBadVersion(midVersion)) {
                if(isBadVersion(midVersion-1)) {
                    rightVersion = midVersion-1;
                } else {
                    return midVersion;
                }
            } else {
                leftVersion = midVersion + 1;
            }
        }
        return midVersion;
    };
};