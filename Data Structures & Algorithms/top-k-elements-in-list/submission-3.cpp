class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> result;
        map<int, int> numToFreq;

        for (int i = 0; i < nums.size(); i++) {
            if (numToFreq.find(nums.at(i)) == numToFreq.end()) {
                numToFreq[nums.at(i)] = 1;
            }
            else {
                numToFreq[nums.at(i)]++;
            }
        }

        map<int, set<int>> freqToNum;
        map<int, int>::iterator it = numToFreq.begin();

        while (it != numToFreq.end()) {
            if (freqToNum.find(it->second) == freqToNum.end()) {
                set<int> toAdd;
                toAdd.insert(it->first);
                freqToNum[it->second] = toAdd;
            }
            else {
                freqToNum[it->second].insert(it->first);
            }
            it++;
        }

        map<int, set<int>>::reverse_iterator it2 = freqToNum.rbegin();
        queue<int> topK;

        while (it2 != freqToNum.rend()) {
            set<int>::iterator it3 = it2->second.begin();
            while (it3 != it2->second.end()) {
                topK.push(*it3);
                it3++;
            }
            it2++;
        }

        int count = 0;
        while (!topK.empty() && count < k) {
            result.push_back(topK.front());
            topK.pop();
            count++;
        }
        return result;
    }
};
