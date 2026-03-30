class Solution {
public:
    void generate(string currString, int open, int closed, vector<string>& currComs, int n) {
        if(open == n && open == closed) {
            currComs.push_back(currString);
        }
        else if (open == closed) {
            currString += "(";
            generate(currString, open + 1, closed, currComs, n);
        }
        else if (open == n) {
            currString += ")";
            generate(currString, open, closed + 1, currComs, n);
        }
        else {
            generate(currString + ")", open, closed + 1, currComs, n);
            generate(currString + "(", open + 1, closed, currComs, n);
        }
    }
    vector<string> generateParenthesis(int n) {
        vector<string> result;
        generate("", 0, 0, result, n);
        return result;
    }
};
