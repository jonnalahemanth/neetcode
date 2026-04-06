class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ch_map = {')':'(',
                   '}':'{',
                    ']':'['}
        for ch in s:
            if ch in ch_map.get(ch, ch)==ch:
                stack.append(ch)
            elif not stack or stack.pop() != ch_map.get(ch):
                return False

        return len(stack) == 0
        