class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        def get_freq(word):
            chars = [0]*26
            for ch in word:
                chars[ord(ch)-ord('a')] += 1

            return chars

        return get_freq(s) == get_freq(t)