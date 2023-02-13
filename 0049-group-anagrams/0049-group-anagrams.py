class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for str in strs:
            count = [0] * 26 # [a ... z]

            for char in str:
                # used character ordance to get the idx of count list
                # Ex: ord('a') - ord('a') = 0
                # Ex: ord('a') - ord('z') = 26
                count[ord(char) - ord('a')] += 1

            anagrams[tuple(count)].append(str)

        return anagrams.values()