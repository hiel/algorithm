import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        Solution s = new Solution();

        int[] nums = {}; int target = 0;
        nums = new int[]{2,7,11,15}; target = 9;
        System.out.println(Arrays.toString(s.twoSum(nums, target)));
        nums = new int[]{3,2,4}; target = 6;
        System.out.println(Arrays.toString(s.twoSum(nums, target)));
        nums = new int[]{3,3}; target = 6;
        System.out.println(Arrays.toString(s.twoSum(nums, target)));
        nums = new int[]{-1,-2,-3,-4,-5}; target = -8;
        System.out.println(Arrays.toString(s.twoSum(nums, target)));
    }

    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            int n = nums[i];
            for (int j = i+1; j < nums.length; j++) {
                int n2 = nums[j];
                if (target == n + n2) {
                    int[] r = {i, j};
                    return r;
                }
            }
        }
        return null;
    }
}
