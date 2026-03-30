class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord('a') - ord(char)] = count[ord('a') - ord(char)] + 1
            if tuple(count) in res:
                res[tuple(count)].append(word)
            else:
                toAdd = []
                toAdd.append(word)
                res[tuple(count)] = toAdd

        return list(res.values())