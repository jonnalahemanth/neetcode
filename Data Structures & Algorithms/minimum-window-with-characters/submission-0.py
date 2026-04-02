class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n1, n2 = len(s), len(t)

        if n2>n1:
            return ""
        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0)+1
        
        need_count = len(need)
        window = {}
        have = 0
        left = 0

        res_len = float('inf')
        res = [-1, -1]

        for right in range(n1):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                have += 1

            while have == need_count:
                if (right-left+1) < res_len:
                    res = [left, right]
                    res_len = right-left+1

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
                
                left += 1


        l, r = res
        return s[l:r+1] if res_len != float('inf') else ""
        