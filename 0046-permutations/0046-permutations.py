class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        
        # base case
        if (len(nums) == 1):
            return [nums.copy()]
        
        for num in nums:
            n = nums.pop(0)
            perms = self.permute(nums)
            
            for perm in perms:
                perm.append(n)
            permutations.extend(perms)
            nums.append(n)
            
        return permutations