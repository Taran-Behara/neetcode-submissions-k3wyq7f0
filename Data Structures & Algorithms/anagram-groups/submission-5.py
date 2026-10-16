class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        word_map = {}
        for word in strs:
            tup = [0] * 26
            for s in word:
                ind = ord('a') - ord(s)
                tup[ind] += 1
            
            tup = tuple(tup)

            if tup in word_map:
                word_map[tup].append(word)
            else:
                word_map[tup] = []
                word_map[tup].append(word)
        
        res = []
        for key in word_map:
            toAdd = word_map[key]
            res.append(toAdd)
        
        return res