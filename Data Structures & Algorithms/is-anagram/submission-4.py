class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        char_s = [0] * 26
        char_t = [0] * 26
        
        for i in range(len(s)):
            char_s[ord(s[i]) - ord('a')] += 1
            char_t[ord(t[i]) - ord('a')] += 1
        

        return char_s == char_t