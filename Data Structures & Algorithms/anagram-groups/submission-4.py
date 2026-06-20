class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        from collections import defaultdict

        hashmap = defaultdict(list)

        for s in strs:
            char_arr = [0] * 26
            for c in s:
                char_arr[ord(c) - ord('a')] += 1
            hashmap[tuple(char_arr)].append(s)
        

        return list(hashmap.values())