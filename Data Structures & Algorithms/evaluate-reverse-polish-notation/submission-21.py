class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == "+":
                one, two = stack.pop(), stack.pop()
                stack.append(one + two) 
            elif t == "*":
                one, two = stack.pop(), stack.pop()
                stack.append(one * two) 
            elif t == "-":
                one, two = stack.pop(), stack.pop()
                stack.append(two - one) 
            elif t == "/":
                one, two = stack.pop(), stack.pop() 
                stack.append(int(two / one))
            else:
                stack.append(int(t))
        
        return stack[len(stack) - 1]
