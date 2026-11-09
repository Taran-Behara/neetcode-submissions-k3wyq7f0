class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        cMap = {}
        cMap["("] = ")"
        cMap["["] = "]"
        cMap["{"] = "}"


        for c in s:
            if c in cMap:
                stack.append(c)
            else:
                if not stack:
                    return False
                
                if cMap[stack[len(stack) - 1]] == c:
                    stack.pop()
                else:
                    return False

        return not stack