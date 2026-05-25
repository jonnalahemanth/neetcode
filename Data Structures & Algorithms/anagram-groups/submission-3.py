from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def freq_str(word):
            chars = [0]*26

            for ch in word:
                chars[ord(ch)-ord('a')] += 1
            
            return tuple(chars)

        anagrams = defaultdict(list)
        
        for item in strs:
            anagrams[freq_str(item)].append(item)

        return list(anagrams.values())

        