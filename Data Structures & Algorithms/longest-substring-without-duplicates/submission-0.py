class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0

        char_set = set()
        n = len(s)

        for r in range(n):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            w = (r - l) + 1
            longest = max(longest, w)
            char_set.add(s[r])
        
        return longest
            



