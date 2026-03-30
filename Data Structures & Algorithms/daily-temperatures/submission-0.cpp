class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<vector<int>> temps;
        vector<int> result(temperatures.size());
        for (int i = 0; i < temperatures.size(); i++) {
            if (temps.empty() || temperatures.at(i) <= temps.top().at(0)) {
                vector<int> toAdd;
                toAdd.push_back(temperatures.at(i));
                toAdd.push_back(i);
                temps.push(toAdd);
            }
            else {
                while (!temps.empty() && temps.top().at(0) < temperatures.at(i)) {
                    result.at(temps.top().at(1)) = i - temps.top().at(1);
                    temps.pop();
                }
                vector<int> toAdd;
                toAdd.push_back(temperatures.at(i));
                toAdd.push_back(i);
                temps.push(toAdd);
            }
        }

        //
        while (!temps.empty()) {
            result.at(temps.top().at(1)) = 0;
            temps.pop();
        }
        return result;
    }
};
