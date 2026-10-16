class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res = res + str(len(word))
            res = res + "#"
            res = res + word
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        index = 0
        while index < len(s):
            j = index
            while s[j] != "#":
                j += 1
            
            length = int(s[index:j])

            k = j + 1
            word = ""
            while len(word) < length:
                word += s[k]
                k += 1
            
            res.append(word)
            index = k

        return res
            