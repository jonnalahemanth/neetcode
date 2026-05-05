from collections import defaultdict
import heapq
from typing import List

class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        res = []

        # inlcude self
        self.following[userId].add(userId)

        # push latest tweet of each followee
        for user in self.following[userId]:
            if self.tweets[user]:
                time, tweetId = self.tweets[user][-1]
                idx = len(self.tweets[user])-1
                heapq.heappush(heap, (-time, tweetId, user, idx))

        # extract top 10

        while heap and len(res)<10:
            time, tweetId, user, idx =heapq.heappop(heap)
            res.append(tweetId)

            if idx>0:
                next_time, next_tweet = self.tweets[user][idx-1]
                heapq.heappush(heap, (-next_time, next_tweet, user, idx-1))
        
        return res
        


        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)

