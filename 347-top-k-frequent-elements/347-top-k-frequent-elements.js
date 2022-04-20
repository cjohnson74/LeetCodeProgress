/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
  const map = new Map(); //! map to count the frequency of the number
  for (let num of nums) {
    map.set(num, map.get(num) + 1 || 1);
  }
  const result = [];
  for (let [key, value] of map) {
    result.push([key, value]); //! add the number and its frequency
  }
  result.sort((a, b) => b[1] - a[1]); //! solve with respect to the frequency of the number
  return result.slice(0, k).map((x) => x[0]); //! slice the list with respect to length of k
};
