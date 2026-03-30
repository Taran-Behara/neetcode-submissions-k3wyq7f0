class MinStack {
private:
stack<int> vals;
stack<int> minStack;
public:
    MinStack() {
    }
    
    void push(int val) {
        vals.push(val);
        if (minStack.empty() || val <= minStack.top()) {
            minStack.push(val);
        }
    }
    
    void pop() {
        if (!vals.empty() && !minStack.empty() && vals.top() == minStack.top()) {
            minStack.pop();
        }
        if (!vals.empty()) {
            vals.pop();
        }
    }
    
    int top() {
        return vals.top();
    }
    
    int getMin() {
        return minStack.top();
    }
};
