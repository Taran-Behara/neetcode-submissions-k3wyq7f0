class Solution:
    def isValid(self, s: str) -> bool:
        match = {}
        match[")"] = "("
        match["]"] = "["
        match["}"] = "{"

        stack = []

        for char in s:
            if char not in match:
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack[len(stack) - 1]
                if match[char] == top:
                    stack.pop()
                else:
                    return False
        
        return not stack
                