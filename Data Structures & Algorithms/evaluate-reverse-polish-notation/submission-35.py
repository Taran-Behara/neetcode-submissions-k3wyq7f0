class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            #print(stack)
            if t == "+" or t == "-" or t == "*" or t == "/":
                numOne = stack[-1]
                stack.pop()
                numTwo = stack[-1]
                stack.pop()

                if t == "+":
                    stack.append(numTwo + numOne)
                elif t == "-":
                    stack.append(numTwo - numOne)
                elif t == "*":
                    stack.append(numTwo * numOne)
                else:
                    res = abs(numTwo) // abs(numOne)
                    if numOne < 0:
                        res *= -1
                    if numTwo < 0:
                        res *= -1
                    stack.append(res)
            else:
                stack.append(int(t))
        
        print(stack)
        return stack[-1]