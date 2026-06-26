from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def get_freq_count(word):
            chars = [0]*26
            for ch in word:
                chars[ord(ch)-ord('a')] += 1

            return tuple(chars)
        word_dict = defaultdict(list)
        for word in strs:
            word_dict[get_freq_count(word)].append(word)

        return list(word_dict.values())


        