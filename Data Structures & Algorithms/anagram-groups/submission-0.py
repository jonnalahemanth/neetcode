from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_strs = defaultdict(list)

        def sort_str(s):
            chars = []
            for ch in s:
                chars.append(ch)
            
            chars.sort()
            return "".join(chars)

        for text in strs:
            hash_strs[sort_str(text)].append(text)

        return [value for _, value in hash_strs.items()]

        