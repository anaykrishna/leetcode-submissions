class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l = 0, r = 1;
        int ans = 0;
        while (r < prices.size()){
            if (prices[l] < prices[r]){
                int curr = prices[r] - prices[l];
                ans = max(ans, curr);
            }
            else{
                l = r;
            }
            r++;
        }
        return ans;
    }
};
