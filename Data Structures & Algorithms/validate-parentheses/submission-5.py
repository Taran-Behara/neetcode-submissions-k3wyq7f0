class Solution:
    def isValid(self, s: str) -> bool:
        t = []

        match = {}
        match["("] = ")"
        match["["] = "]"
        match["{"] = "}"

        for char in s:
            if char in match:
                t.append(char)
            elif t == [] or match[t[len(t) - 1]] != char:
                return False
            else:
                t.pop()
        return t == []   