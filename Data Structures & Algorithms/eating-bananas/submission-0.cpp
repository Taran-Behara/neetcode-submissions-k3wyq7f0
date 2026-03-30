class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int maxNum = 0;
        for (int i = 0; i < piles.size(); i++) {
            if (piles.at(i) > maxNum) {
                maxNum = piles.at(i);
            }
        }

        int start = 1;
        int end = maxNum;
        int mid;
        int currMin = INT_MAX;
        while (start <= end) {
            mid = start + ((end - start)/2);
            cout << mid << endl;
            unsigned int sum = 0;
            for (int i = 0; i < piles.size(); i++) {
                double toAdd = (double)piles.at(i)/mid;
                int hours = ceil(toAdd);
                sum += hours;
            }
            if (sum <= h) {
                if (mid < currMin) {
                    currMin = mid;
                }
                end = mid - 1;
            }
            else {
                start = mid + 1;
            }
        }
        return currMin;
    }
};
