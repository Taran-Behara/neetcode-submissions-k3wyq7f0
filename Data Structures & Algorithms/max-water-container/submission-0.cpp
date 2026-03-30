class Solution {
public:
    int maxArea(vector<int>& heights) {
        int left = 0;
        int right = heights.size() - 1;
        int currMax = 0;
        while(left < right) {
            int h;
            if(heights.at(left) < heights.at(right)) {
                h = heights.at(left);
            }
            else {
                h = heights.at(right);
            }
            int w = right - left;
            int amount = w * h;
            if (amount > currMax) {
                currMax = amount;
            }

            if (heights.at(left) < heights.at(right)) {
                left++;
            }
            else {
                right--;
            }
        }
        return currMax;
    }
};
