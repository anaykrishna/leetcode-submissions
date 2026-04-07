class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map <char, int> freq;
        for (int i = 0 ; i < nums.size() ; i++){
            freq[nums[i]]++;
        }

        vector<pair<char, int>> vec(freq.begin(), freq.end());

        sort(vec.begin(), vec.end(), [](pair<char, int> &a, pair<char, int> &b){
            return a.second > b.second;
        });

        vector<int> ans;
        for(int i = 0 ; i < k ; i++){
            ans.push_back(vec[i].first);
        }

        return ans;
    }
};
