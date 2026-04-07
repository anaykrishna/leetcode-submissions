class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int l = 0, ans = 0;
        set<char> window;

        for (int r = 0 ; r < s.size() ; r++){
            while (l < r && window.find(s[r]) != window.end()){
                window.erase(s[l]);
                l++;
            }

            window.insert(s[r]);
            ans = max(ans, (int)window.size());
            
        }

        return ans;
    }
};
