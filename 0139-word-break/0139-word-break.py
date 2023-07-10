class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp
        # dfs
        # loop through wordDict
            # check if s[i:len(word)] == word
                # dfs(i + len(word))
        # base case if i == len(s)
            # return True
        # base case if i > len(s)
            # return False
        # return False
        
        # dp
        # dp array of length (len(s) + 1) all False
        # dp[len(s)] = True
        # go through all indexes starting at len(s)-1 to 0
        # loop through each word in words
        # if index + len(word) <= len(s) and s[index:index+len(word)] == word
        #     dp[index] = dp[index + len(w)]
        #     if dp[index]:
        #     break
        # return dp[0]
        
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if i + len(word) <= len(s) and s[i:i+len(word)] == word:
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    break
                    
        return dp[0]
        
        
        
#         def dfs(i, memo = {}):
#             if i in memo:
#                 return memo[i]
            
#             if i == len(s):
#                 return True
            
#             if i > len(s):
#                 return False
            
#             res = False
#             for word in wordDict:
#                 if ((i + len(word)) <= len(s)) and s[i:len(word)] == word:
#                     if (dfs(i + len(word))):
#                         res = True
#             memo[i] = res
#             return res
        
#         return dfs(0)