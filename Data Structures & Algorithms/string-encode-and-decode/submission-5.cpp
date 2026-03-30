class Solution {
public:

    string encode(vector<string>& strs) {
        string result = "";
        for (int i = 0; i < strs.size(); i++) {
            result += to_string(strs.at(i).length());
            result += "#";
            result += strs.at(i);
        }
        return result;
    }

    vector<string> decode(string s) {
        bool foundHash = false;
        string num = "";
        vector<string> result;
        cout << s << endl;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '#' && i == s.length() - 1) {
                result.push_back("");
                return result;
            }
            if (s[i] == '#' && !foundHash) {
                foundHash = true;
                continue;
            }

            if (!foundHash) {
                num += s[i];
                continue;
            }
            else {
                cout << "Num: " << num << endl;
                int length = stoi(num);
                string word = s.substr(i, length);
                result.push_back(word);
                num = "";
                foundHash = false;
                i += length - 1;
            }
        }
        return result;
    }


};
