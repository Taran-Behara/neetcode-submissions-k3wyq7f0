class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> numStack;
        int result = 0;

        for (int i = 0; i < tokens.size(); i++) {
            if (tokens.at(i) == "+" || tokens.at(i) == "-" || tokens.at(i) == "*" || tokens.at(i) == "/") {
                int numTwo = numStack.top();
                numStack.pop();
                int numOne = numStack.top();
                numStack.pop();

                if (tokens.at(i) == "+") {
                    result = numOne + numTwo;
                }
                else if (tokens.at(i) == "-") {
                    result = numOne - numTwo;
                }
                else if (tokens.at(i) == "*") {
                    result = numOne * numTwo;
                }
                else if (tokens.at(i) == "/") {
                    result = numOne / numTwo;
                }
                numStack.push(result);
            }
            else {
                numStack.push(stoi(tokens.at(i)));
            }
        }
        return numStack.top();
    }
};
