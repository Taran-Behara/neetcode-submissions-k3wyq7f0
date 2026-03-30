class Solution {
public:
    bool isValid(string s) {
        map<char, char> checkValid;
        checkValid['('] = ')';
        checkValid['{'] = '}';
        checkValid['['] = ']';

        stack<char> strStack;

        for (int i = 0; i < s.length(); i++) {
            if (s[i] != ')' && s[i] != ']' && s[i] != '}') {
                strStack.push(s[i]);
            }
            else {
                if (strStack.empty()) {
                    return false;
                }
                if (checkValid[strStack.top()] != s[i]) {
                    return false;
                }
                else {
                    strStack.pop();
                }
            }
        }

        if (strStack.empty()) {
            return true;
        }
        return false;
    }
};
