class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def hash_str(str1):
            hash_map = {}
            for ch in str1:
                if ch in hash_map:
                    hash_map[ch] += 1
                else:
                    hash_map[ch] = 1
            return hash_map
        hash_t = hash_str(t)
        hash_s = hash_str(s)
        print(hash_t, hash_s)
        if len(hash_t)!= len(hash_s):
            return False
        for key,value in hash_s.items():
            if key not in hash_t:
                return False
            if key in hash_t and hash_t[key] != value:
                return False
        return True