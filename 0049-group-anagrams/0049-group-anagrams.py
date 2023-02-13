class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = [] # return variable
        anagramsMap = {} # Ex: {'aet': ['ate', 'eat', 'tea']}

        # loop through string list
            # sort each string in assending order
            # add string to anagram map using sorted string as key
        for str in strs:
            sortedStr = ''.join(sorted(str))
            print(sortedStr)
            if sortedStr not in anagramsMap:
                anagramsMap[sortedStr] = []
            anagramsMap[sortedStr].append(str)
        
        # loop through anagramsMap pushing each array to anagrams
        for key in anagramsMap:
            anagrams.append(anagramsMap[key])

        # return anagrams
        return anagrams