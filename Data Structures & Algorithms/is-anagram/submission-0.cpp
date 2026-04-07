class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size())   return false;

        map<char, int> freq;
        for (int i = 0 ; i < s.size() ; i++){
            freq[s[i]]++;
        }

        for (int i = 0 ; i < t.size() ; i++){
            freq[t[i]]--;
        }

        for(auto &it: freq){
            if (it.second != 0)   return false;
        }
    
        return true;
    }
};
