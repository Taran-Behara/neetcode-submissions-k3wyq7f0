class Solution {
public:
    int find(vector<int>& nums, int start, int end) {
        if (start >= end) {
            return nums.at(start);
        }
        int mid = start + ((end - start)/2);
        int curr = nums.at(mid);
        if (mid - 1 >= 0 && mid + 1 < nums.size() && curr < nums.at(mid - 1) &&
         curr < nums.at(mid + 1)) {
            return curr;
        }
        int one = find(nums, mid + 1, end);
        int two = find(nums, start, mid - 1);
        if (one < two) {
            return one;
        }
        return two;
    }
    int findMin(vector<int> &nums) {
        return find(nums, 0, nums.size() - 1);
    }
};
