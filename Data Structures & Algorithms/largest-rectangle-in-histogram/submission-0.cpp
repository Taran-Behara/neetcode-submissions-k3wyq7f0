class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        stack<vector<int>> nums;
       int maxArea = 0;
       for (int i = 0; i < heights.size(); i++) {
          if (nums.empty() || heights.at(i) >= nums.top().at(1)) {
            vector<int> toAdd;
            toAdd.push_back(i);
            toAdd.push_back(heights.at(i));
            nums.push(toAdd);
          }
          else {
            int count = 0;
            int startVal = i;
            while (!nums.empty() && heights.at(i) < nums.top().at(1)) {
                int area = (i - nums.top().at(0)) * nums.top().at(1);
                if (area > maxArea) {
                    maxArea = area;
                }
                if (nums.top().at(1) >= heights.at(i)) {
                    count++;
                    startVal = nums.top().at(0);
                }
                nums.pop();
            }
            vector<int> toAdd;
            toAdd.push_back(startVal);
            toAdd.push_back(heights.at(i));
            nums.push(toAdd);
          }
       }
       while (!nums.empty()) {
        int area = (heights.size() - nums.top().at(0)) * nums.top().at(1);
        if (area > maxArea) {
            maxArea = area;
        }
        nums.pop();
       }
       return maxArea;
    }
};
