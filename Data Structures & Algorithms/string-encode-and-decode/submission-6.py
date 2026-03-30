class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res = res + str(len(word)) + "#" + word
        print(res)
        return res
    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j = j + 1
            length = s[i:j]

            res.append(s[j + 1:j + 1 + int(length)])
            i = j + 1 + int(length)
        return res