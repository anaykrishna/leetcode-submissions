class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        return "#".join(f"{len(s)}:{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        ans = []
        i = 0
        n = len(s)
        while i < n:
            sep_index = s.find(":", i)
            if sep_index == -1:
                break

            length = int(s[i:sep_index])
            st = sep_index + 1
            end = st + length
            ans.append(s[st:end])

            i = end + 1 
        return ans
        
        
