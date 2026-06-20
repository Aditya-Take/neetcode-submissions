class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        from collections import Counter

        count_s = Counter(s)
        count_t = Counter(t)

        for c in count_s:
            if count_s[c] != count_t.get(c,0):
                return False

        return True    