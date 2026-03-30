class Solution {
public:
int find (vector<int>& nums, int start, int end, int target) {
        if (start >= end) {
            if (nums.at(start) == target) {
                return start;
            }
            return -1;
        }

        int mid = start + ((end - start)/2);
        if (nums.at(mid) == target) {
            return mid;
        }

        int numOne = find(nums, start, mid - 1, target);
        int numTwo = find(nums, mid + 1, end, target);

        if (numOne < 0 && numTwo < 0) {
            return -1;
        }
        else if (numOne < 0) {
            return numTwo;
        }
        return numOne;
    }
    int search(vector<int>& nums, int target) {
        return find(nums, 0, nums.size() - 1, target);
    }
};
