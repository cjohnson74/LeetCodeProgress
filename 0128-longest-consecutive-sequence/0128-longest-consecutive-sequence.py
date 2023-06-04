class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) is 0:
            return 0
        numSet = set(nums)
        startVals = []
        maxLen = 0
        
        for currVal in numSet:
            if currVal-1 not in numSet:
                startVals.append(currVal)
        
        for currStartVal in startVals:
            currVal = currStartVal
            currSeqLen = 1
            while True:
                currVal += 1
                if currVal not in numSet:
                    maxLen = max(currSeqLen, maxLen)
                    break;
                else:
                    currSeqLen += 1
                    
        maxLen = max(maxLen, currSeqLen)
        return maxLen