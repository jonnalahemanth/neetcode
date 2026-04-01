class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        def freq_count(s):
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            return count

        s1_count = freq_count(s1)
        window_count = freq_count(s2[:n1])

        if s1_count == window_count:
            return True

        for i in range(n1, n2):
            # add new char
            window_count[ord(s2[i]) - ord('a')] += 1
            # remove old char
            window_count[ord(s2[i - n1]) - ord('a')] -= 1

            if s1_count == window_count:
                return True

        return False
        