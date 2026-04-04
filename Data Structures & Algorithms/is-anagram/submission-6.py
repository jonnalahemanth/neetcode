class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def get_freq_count(s1):
            freq = [0]*26

            for ch in s1:
                freq[ord(ch)-ord('a')] += 1
            
            return freq

        return get_freq_count(s) == get_freq_count(t)