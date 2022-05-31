/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    var arrayNumber = BigInt(digits.join(''));
    console.log(arrayNumber);
    arrayNumber++;
    console.log(arrayNumber);
    var digitsUpdated = arrayNumber.toString().split('').map((digit) => parseInt(digit));
    return digitsUpdated;
};