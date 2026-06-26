class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def get_freq_count(word):
            chars = [0]*26

            for ch in word:
                chars[ord(ch)-ord('a')] += 1
            
            return chars

        return get_freq_count(s) == get_freq_count(t)
        