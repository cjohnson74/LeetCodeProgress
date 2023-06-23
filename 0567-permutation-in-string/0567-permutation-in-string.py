class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        # map s1
        mapS1 = {}
        matches = 0
        for lett in s1:
            mapS1[lett] = mapS1.get(lett, 0) + 1
            
        left = 0
        right = len(s1) - 1
        window = {}
        for i in range(len(s1)):
            window[s2[i]] = window.get(s2[i], 0) + 1
            if s2[i] in mapS1:
                if window[s2[i]] == mapS1[s2[i]]:
                    matches += 1
                    
        
        for r in range(len(s1), len(s2)):
            if matches == len(mapS1):
                return True
            if s2[left] in mapS1:
                if window[s2[left]] == mapS1[s2[left]]:
                    matches -= 1
            window[s2[left]] -= 1
            left += 1
            currLett = s2[r]
            window[currLett] = window.get(currLett, 0) + 1
            if currLett in mapS1:
                if window[currLett] == mapS1[currLett]:
                    matches += 1
                
        return matches == len(mapS1)
            
                
            