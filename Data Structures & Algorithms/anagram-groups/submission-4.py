class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                chash = ord(c) - ord('a')
                count[chash] += 1
            
            key = tuple(count)
            if key in hashmap:
                hashmap[key].append(s)
            else:
                hashmap[key] = [s]
        
        res = []

        for key in hashmap:
            toAdd = []
            for s in hashmap[key]:
                toAdd.append(s)
            
            res.append(toAdd)
        

        return res