class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map <string, vector<string>> mp;

        for (auto &w : strs){
            string key = w;
            sort(key.begin(), key.end());
            mp[key].push_back(w);
        }

        vector<vector<string>> result;
        for (auto &it : mp){
            result.push_back(it.second);
        }

        return result;
    }
};
