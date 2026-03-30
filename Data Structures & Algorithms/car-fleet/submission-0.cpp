class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        map<int, int> posSpeed;
        for (int i = 0; i < position.size(); i++) {
            posSpeed[position.at(i)] = speed.at(i);
        }
        sort(position.begin(), position.end());
        map<int, double> indToTime;
        for (int i = 0; i < position.size(); i++) {
            double distance = (double)target - (double)position.at(i);
            double speed = (double) posSpeed[position.at(i)];
            indToTime[i] = distance / speed;
        }

        cout << "Test: " << indToTime[1] << endl;

        int right = position.size() - 1;
        int left = right - 1;
        int numFleets = 1;
        while (left >= 0 && right >= 0) {
            if (indToTime[left] > indToTime[right]) {
                right = left;
                left--;
                numFleets++;
            }
            else {
                left--;
            }
        }
        return numFleets;
    }
};
