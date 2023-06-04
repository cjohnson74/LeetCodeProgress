class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) is 0:
            return 0
        numSet = set(nums)
        maxLen = 0
        
        for currVal in numSet:
            if currVal-1 not in numSet:
                currSeqLen = 0
                while currVal+currSeqLen in numSet:
                    currSeqLen += 1
                maxLen = max(maxLen, currSeqLen)

        return maxLen