class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        map<int, vector<int>> dp;
        vector<int> result;
        vector<int> p1;
        dp[0] = p1;
        dp[0].push_back(1);
        for (int i = 1; i < nums.size(); i++) {
            vector<int> products;
            dp[i] = products;
            dp[i].push_back(dp[i - 1].at(0) * nums.at(i - 1));
        }

        dp[nums.size() - 1].push_back(1);
        for (int i = nums.size() - 2; i >= 0; i--) {
            dp[i].push_back(dp[i + 1].at(1) * nums.at(i + 1));
        }

        for (int i = 0; i < nums.size(); i++) {
            result.push_back(dp[i].at(0) * dp[i].at(1));
        }
        return result;
    }
};
