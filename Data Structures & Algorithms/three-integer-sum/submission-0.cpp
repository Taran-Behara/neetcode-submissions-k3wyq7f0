class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> sNums = nums;
        set<int> seenNums;
        sort(sNums.begin(), sNums.end());

        for (int i = 0; i < sNums.size(); i++) {
            if(seenNums.find(sNums.at(i)) != seenNums.end()) {
                continue;
            }
            seenNums.insert(sNums.at(i));
            int left = i + 1;
            int right = sNums.size() - 1;

            set<int> seen;
            int target = 0 - sNums.at(i);
            while (left < right) {
                int sum = sNums.at(left) + sNums.at(right);
                if (sum > target) {
                    right--;
                }
                else if (sum < target) {
                    left++;
                }
                else {
                    if (seen.find(sNums.at(left)) == seen.end()) {
                        vector<int> toAdd;
                        toAdd.push_back(sNums.at(i));
                        toAdd.push_back(sNums.at(left));
                        toAdd.push_back(sNums.at(right));
                        result.push_back(toAdd);
                        seen.insert(sNums.at(left));
                    }
                    left++;
                    right--;
                }
            }
        }
        return result;
    }
};
