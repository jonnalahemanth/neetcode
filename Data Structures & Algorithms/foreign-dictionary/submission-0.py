from collections import defaultdict, deque
from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(set)

        indegree = {}

        # add all unique chars
        for word in words:
            for ch in word:
                indegree[ch] = 0

        # buld graph
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]

            if len(w1)>len(w2) and w1.startswith(w2):
                return ""

            min_len = min(len(w1), len(w2))

            for j in range(min_len):
                if w1[j] != w2[j]:
                    parent = w1[j]
                    child = w2[j]

                    if child not in graph[parent]:
                        graph[parent].add(child)
                        indegree[child] += 1
                    
                    break

        # topological sort

        q = deque()

        for ch in indegree:
            if indegree[ch] == 0:
                q.append(ch)

        order = []

        while q:
            ch = q.popleft()
            order.append(ch)

            for nei in graph[ch]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)

        
        # cycle detection
        if len(order) != len(indegree):
            return ""

        return "".join(order)