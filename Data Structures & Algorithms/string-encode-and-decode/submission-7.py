class Solution:
    # #5Hello#5World
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        res = []

        index = 0
        while index < len(s):
            j = index
            while s[j] != "#":
                j = j + 1
            length = int(s[index:j])

            word = s[j + 1:j + 1 + length]
            res.append(word)
            index = j + 1 + length
        return res
