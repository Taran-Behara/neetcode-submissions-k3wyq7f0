class Solution {
public:
    int trap(vector<int>& height) {
        map<int, vector<int>> boundaries;
        vector<int> init;
        init.push_back(0);
        boundaries[0] = init;
        int currMax = 0;

        for (int i = 1; i < height.size(); i++) {
            if (height.at(i - 1) > currMax) {
                vector<int> toAdd;
                toAdd.push_back(height.at(i - 1));
                boundaries[i] = toAdd;
                currMax = height.at(i - 1);
            }
            else {
                vector<int> toAdd;
                toAdd.push_back(currMax);
                boundaries[i] = toAdd;
            }
        }

        currMax = 0;
        boundaries[height.size() - 1].push_back(0);

        for (int i = height.size() - 2; i >= 0; i--) {
            if (height.at(i + 1) > currMax) {
                boundaries[i].push_back(height.at(i + 1));
                currMax = height.at(i + 1);
            }
            else {
                boundaries[i].push_back(currMax);
            }
        }

        int sum = 0;
        for (int i = 0; i < height.size(); i++) {
            int maxLeft = boundaries[i].at(0);
            int maxRight = boundaries[i].at(1);
            int useHeight;
            if (maxLeft < maxRight) {
                useHeight = maxLeft;
            }
            else {
                useHeight = maxRight;
            }
            int amount = useHeight - height.at(i);
            if (amount >= 0) {
                sum += amount;
            }
        }
        return sum;
    }
};
