class Solution:
    def numDecodings(self, s: str) -> int:
        # dfs
        # either move once or move twice since integer length cannot be more than 2
        # if index == len(s) - 1: return 1 if currInt in intToChar map else 0
        # if currInt < 0 or currInt >= 27: return 0
        # return dfs(index+1, s[index:index+2]) + dfs(index+2, s[index:index+3])
        dp = { len(s): 1 }
        
        def dfs(index):
            if index in dp:
                return dp[index]

            if s[index] == '0': 
                return 0
            
            res = dfs(index + 1)
            
            if (index + 1 < len(s) and (s[index] == '1' or s[index] == '2' and s[index + 1] in '0123456')):
                res += dfs(index + 2)
            dp[index] = res
            return res
        
        return dfs(0)
                                                 
        