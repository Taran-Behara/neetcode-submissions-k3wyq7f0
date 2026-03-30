class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char, int> seenChars;
        for (int i = 0; i < s.length(); i++) {
            if (seenChars.find(s[i]) == seenChars.end()) {
                seenChars[s[i]] = 1;
            }
            else {
                seenChars[s[i]]++;
            }
        }

        for (int i = 0; i < t.length(); i++) {
            if (seenChars.find(t[i]) == seenChars.end() || seenChars[t[i]] == 0) {
                return false;
            }
            else {
                seenChars[t[i]]--;
            }
        }
        
        map<char, int>::iterator it = seenChars.begin();
        while (it != seenChars.end()) {
            if (it->second != 0) {
                return false;
            }
            it++;
        }
        return true;
    }
};
