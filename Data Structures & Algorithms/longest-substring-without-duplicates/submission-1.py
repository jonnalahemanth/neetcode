class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        max_len = 0
        n = len(s)
        hash_map = {}

        while right<n:
            ch = s[right]
            if ch in hash_map:
                left = max(left, hash_map[ch]+1)
            hash_map[ch] = right
            max_len = max(max_len, right-left+1)
            right +=1

        return max_len