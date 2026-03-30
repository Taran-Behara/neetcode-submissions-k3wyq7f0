class TimeMap {
private:
    map<string, vector<pair<string, int>>> data;
public:
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        pair<string, int> toAdd;
        toAdd.first = value;
        toAdd.second = timestamp;
        if (data.find(key) == data.end()) {
            vector<pair<string, int>> assign;
            assign.push_back(toAdd);
            data[key] = assign;
        }
        else {
            data[key].push_back(toAdd);
        }
    }
    
    string get(string key, int timestamp) {
        if (data.find(key) == data.end()) {
            return "";
        }

        string closestResult = "";
        vector<pair<string, int>> toCheck = data[key];

        int start = 0;
        int end = toCheck.size() - 1;

        while (start <= end) {
            int mid = start + ((end - start)/2);
            if (toCheck.at(mid).second == timestamp) {
                return toCheck.at(mid).first;
            }
            else if (toCheck.at(mid).second > timestamp) {
                end = mid - 1;
            }
            else {
                start = mid + 1;
                closestResult = toCheck.at(mid).first;
            }
        }

        return closestResult;
    }
};
