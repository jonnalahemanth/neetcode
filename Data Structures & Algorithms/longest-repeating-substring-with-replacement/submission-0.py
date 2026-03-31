from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_len = 0
        max_freq = 0
        ch_freq = defaultdict(int)

        for right, ch in enumerate(s):
            ch_freq[ch] += 1
            max_freq = max(max_freq, ch_freq[ch])
 
            while (right-left+1) - max_freq>k:
                ch_freq[s[left]] -=1
                left += 1
            max_len = max(max_len, right-left+1)
        
        return max_len
        