from collections import defaultdict


class CountSquares:
    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        res = 0

        # IMPORTANT: convert to list to freeze iteration
        for (x2, y2), cnt in list(self.points.items()):
            if x2 == x1 and y2 != y1:
                side = y2 - y1

                # right side square
                p1 = (x1 + side, y1)
                p2 = (x2 + side, y2)

                res += cnt * self.points.get(p1, 0) * self.points.get(p2, 0)

                # left side square
                p1 = (x1 - side, y1)
                p2 = (x2 - side, y2)

                res += cnt * self.points.get(p1, 0) * self.points.get(p2, 0)

        return res
