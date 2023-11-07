class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arrivalTimes = sorted([(dist[i] / speed[i]) for i in range(len(dist))])
        count = 0;
        for i in range(len(arrivalTimes)):
            if (arrivalTimes[i] <= float(i)):
                return count
            count += 1
        return count