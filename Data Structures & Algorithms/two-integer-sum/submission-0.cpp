class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> numToIndex;
        vector<int> result;

        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums.at(i);

            if (numToIndex.find(complement) != numToIndex.end()) {
                result.push_back(numToIndex[complement]);
                result.push_back(i);
                return result;
            }
            else {
                numToIndex[nums.at(i)] = i;
            }
        }
        return result;
    }
};
