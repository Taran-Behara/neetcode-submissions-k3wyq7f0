class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
      set<int> seenNums;
        for (int i = 0; i < nums.size(); i++) {
            seenNums.insert(nums.at(i));
        }
        
        int currMax = 0;
        for (int i = 0; i < nums.size(); i++) {
            bool startStreak = false;
            if (seenNums.find(nums.at(i) - 1) == seenNums.end()){
                startStreak = true;
            }

            if (startStreak) {
                int streakCount = 0;
                int currNum = nums.at(i);
                while (seenNums.find(currNum) != seenNums.end()) {
                    streakCount++;
                    currNum++;
                }
                if (streakCount > currMax) {
                    currMax = streakCount;
                }
            }
        }
        return currMax;  
    }
};
