class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # res += f"{len(s)}#{s}"
            res += f"{str(len(s)).zfill(4)}{s}"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i<len(s):
            length = int(s[i:i+4])
            i += 4
            res.append(s[i:i+length])
            i = i+length
        return res
        # i = 0
        # while i<len(s):
        #     j = i
        #     # extract the length
        #     while s[j] != '#':
        #         j += 1
            
        #     length = int(s[i:j])

        #     word = s[j+1:j+1+length]
        #     res.append(word)

        #     i = j+1+lenth

        # return res
