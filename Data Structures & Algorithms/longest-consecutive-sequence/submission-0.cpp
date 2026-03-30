class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        set<int> numSet;
        for (int i = 0; i < nums.size(); i++) {
            numSet.insert(nums.at(i));
        }

        int currStreak = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (numSet.find(nums.at(i) - 1) == numSet.end()) {
                int streak = 1;
                int nextNum = nums.at(i) + 1;
                while (numSet.find(nextNum) != numSet.end()) {
                    streak++;
                    nextNum++;
                }

                if (streak > currStreak) {
                    currStreak = streak;
                }
            }
        }
        return currStreak;
    }
};
