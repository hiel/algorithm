// https://leetcode.com/problems/running-sum-of-1d-array/

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        for (int i = 1; i < nums.size(); i++) {
            nums[i] += nums[i - 1];
        }
        return nums;
    }
};

void test(vector<int> nums) {
    Solution mySolution = Solution();

    for (auto i: nums)
        cout << i << " ";
    cout << "// ";

    nums = mySolution.runningSum(nums);

    for (auto i: nums)
        cout << i << " ";
    cout << endl;
}

int main() {
    test({1, 2, 3, 4});
    test({1, 1, 1, 1, 1});
    test({3, 1, 2, 10, 1});

    return 0;
}
