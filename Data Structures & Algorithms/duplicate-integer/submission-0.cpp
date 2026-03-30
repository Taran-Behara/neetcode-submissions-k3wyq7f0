class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> seenNums;

        for (int i = 0; i < nums.size(); i++) {
            if (seenNums.find(nums.at(i)) != seenNums.end()) {
                return true;
            }
            seenNums.insert(nums.at(i));
        }
        return false;
    }
};
