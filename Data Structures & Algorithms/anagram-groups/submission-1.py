from collections import defaultdict
import string
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_strs = defaultdict(list)

        def sort_str(s):
            chars = []
            for ch in s:
                chars.append(ch)
            
            chars.sort()
            return "".join(chars)
        
        def hash_str(s):
            hash_map = defaultdict(int)
            res = []

            for ch in s:
                hash_map[ch] += 1

            for ch in string.ascii_lowercase:
                if ch in hash_map:
                    for _ in range(hash_map[ch]):
                        res.append(ch)
            return "".join(res)

        for text in strs:
            hash_strs[hash_str(text)].append(text)

        return [value for _, value in hash_strs.items()]

        