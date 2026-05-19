class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramsMap = {}

        for word in strs:
            wordMap = [0] * 26
            for letter in word:
                index = ord('a') - ord(letter)
                wordMap[index] += 1
            
            wordTup = tuple(wordMap)
            if wordTup in anagramsMap:
                anagramsMap[wordTup].append(word)
            else:
                toAdd = []
                toAdd.append(word)
                anagramsMap[wordTup] = toAdd
        
        res = []
        for key in anagramsMap:
            res.append(anagramsMap[key])
        
        return res