class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []

        anagrams = {}

        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord('a') - ord(char)] = count[ord('a') - ord(char)] + 1
            
            key = tuple(count)
            if key in anagrams:
                anagrams[key].append(s)
            else:
                toAdd = []
                toAdd.append(s)
                anagrams[key] = toAdd
        
        for key in anagrams:
            res.append(anagrams[key])
        
        return res

        