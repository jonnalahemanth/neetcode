class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def freq_str(s1):
            chars = [0]*26
            for ch in s1:
                chars[ord(ch)-ord('a')] += 1
            return chars

        return freq_str(s) == freq_str(t)
        