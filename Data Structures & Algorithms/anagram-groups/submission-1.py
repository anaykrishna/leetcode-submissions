class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            dic[tuple(sorted(s))].append(s)
        
        ans = []
        for k in dic:
            ans.append(dic[k])
        
        return ans

            