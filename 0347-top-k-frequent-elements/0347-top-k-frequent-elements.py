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

        #print(counts)
        # while k > 0
        # loop through counts starting at the end of the counts array
            # if the length of the array at counts[i] is greater than 0
            # pop of each element and add it to topKElem array
            # reduce k by 1
        while k > 0:
            for i in range(len(counts)-1, 0, -1):
                #print(i, counts[i])
                while len(counts[i]) > 0 and k > 0:
                    topKElem.append(counts[i].pop(0))
                    k -= 1

        # return first k indexes of sortedArray
        return topKElem