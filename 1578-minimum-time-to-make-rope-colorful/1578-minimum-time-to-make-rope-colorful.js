/**
 * @param {string} colors
 * @param {number[]} neededTime
 * @return {number}
 */
var minCost = function(colors, neededTime) {
    // totalTime to keep track of total time
    // iterate over each balloon and its preceeding neighbor
    // start at 0 end at < length-1
    // if balloon matches it's next neighbor
    // startIdx to keep track of index to split at
    // currTimes = [];
    // while (ballon matches neighbor)
    // push balloon time using current balloon index and needTime array to currTimes
    // i++
    // after while loop push neededTime[i+1] to currTimes and sort currTimes ascending order
    // for loop through currTimes start at 0 end at < length-1 and add the times to totalTime
    // after for loop return totalTime
    
    var totalTime = 0;
    
    for (let i = 0; i < colors.length-1; i++) {
        if (colors[i] == colors[i+1]) {
            var startIdx = i;
            var currTimes = [];
            while (colors[i] == colors[i+1] && i < colors.length) {
                currTimes.push(neededTime[i]);
                i++;
            }
            currTimes.push(neededTime[i])
            var currTimesSorted = currTimes.sort((a,b) => a-b);
            console.log(currTimes)
            console.log(currTimesSorted);
            for (let j = 0; j < currTimesSorted.length-1; j++) {
                totalTime += currTimesSorted[j];
            }
        }
    }
    
    return totalTime;
};