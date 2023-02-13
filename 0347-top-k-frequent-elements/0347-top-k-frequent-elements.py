class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freqMap
        freqMap = {}

        # counts length of nums and empty array at each idx
        counts = [[] for i in range(len(nums) + 1)]

        print(counts)
        # topKElem = []
        topKElem = []

        # loop through list of integers
        # if integer in freqMap increase value by 1
        for num in nums:
            freqMap[num] = 1 + freqMap.get(num, 0)

        # loop through freqMap
        # add element to counts array counts[freqMap[key]]
        for num, count in freqMap.items():
            counts[count].append(num)
            # print(num, freqMap[num], counts)

        # loop through counts starting at the end of the counts array
            # pop of each element and add it to topKElem array
            # reduce k by 1
        for i in range(len(counts)-1, 0, -1):
            #print(i, counts[i])
            for num in counts[i]:
                topKElem.append(num)
                if len(topKElem) == k:
                    return topKElem
