from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        for num in sorted(count):

            while count[num] >0:

                for i in range(groupSize):
                    nxt = num+i

                    if count[nxt] == 0:
                        return False

                    count[nxt] -= 1

        return True
        