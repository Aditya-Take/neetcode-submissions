class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        from collections import defaultdict

        map = defaultdict(list)

        for s in strs:
            arr = [0]*26
            for c in s:
                arr[ord(c)-ord('a')] += 1

            map[tuple(arr)].append(s)

        return list(map.values())
