class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<map<char, int>, vector<string>> anagrams;
        vector<vector<string>> result;

        for (int i = 0; i < strs.size(); i++) {
            map<char, int> letters;
            string word = strs.at(i);
            for (int j = 0; j < word.length(); j++) {
                if (letters.find(word[j]) == letters.end()) {
                    letters[word[j]] = 1;
                }
                else {
                    letters[word[j]]++;
                }
            }
            if (anagrams.find(letters) == anagrams.end()) {
                vector<string> add;
                add.push_back(word);
                anagrams[letters] = add;
            }
            else {
                anagrams[letters].push_back(word);
            }
        }

        map<map<char, int>, vector<string>>::iterator it = anagrams.begin();
        while (it != anagrams.end()) {
            vector<string> toAdd;
            for (int i = 0; i < it->second.size(); i++) {
                toAdd.push_back(it->second.at(i));
            }
            result.push_back(toAdd);
            it++;
        }
        return result;
    }
};
