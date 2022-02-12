public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        for (int i = 0; i < nums.Length - 1; i++)
        {
            for (int j = nums.Length - 1; j > i; j--)
            {
            if (nums[i] == nums[j])
                return true;
            }
        }
        return false;
    }
}