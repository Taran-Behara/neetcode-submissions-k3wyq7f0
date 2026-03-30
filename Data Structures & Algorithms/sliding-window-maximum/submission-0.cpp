class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        map<int, int> window;
        vector<int> result;
        for (int i = 0; i < k; i++) {
            if (window.find(nums.at(i)) == window.end()) {
                window[nums.at(i)] = 1;
            }
            else{
                window[nums.at(i)]++;
            }
        }

        int max = window.rbegin()->first;
        result.push_back(max);
        int l = 1;
        int r = l + k - 1;

        while (r < nums.size()) {
            window[nums.at(l - 1)]--;
            if (window[nums.at(l - 1)] == 0) {
                window.erase(nums.at(l - 1));
            }

            if (window.find(nums.at(r)) == window.end()) {
                window[nums.at(r)] = 1;
            }
            else {
                window[nums.at(r)]++;
            }

            int max = window.rbegin()->first;
            result.push_back(max);
            l++;
            r++;
        }
        return result;
    }
};
