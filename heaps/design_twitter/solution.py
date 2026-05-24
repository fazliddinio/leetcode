"""
Design Twitter
LeetCode 355

Approach: Hash Maps + Heap
Time: Post: O(1), Follow: O(1), Feed: O(N log K) — Merge K sorted lists.
Space: O(T + F) — T=Total Tweets, F=Total Follows.
Brute: O(T log T) — Collect all followee tweets into one list, sort by time, take top 10.
"""

from typing import List
from collections import defaultdict
import heapq


class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append([-self.time, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []
        self.following[userId].add(userId)
        for followeeId in self.following[userId]:
            if followeeId in self.tweets:
                user_tweets = self.tweets[followeeId]
                index = len(user_tweets) - 1
                time, tweetId = user_tweets[index]
                heapq.heappush(min_heap, (time, tweetId, followeeId, index - 1))
        while min_heap and len(res) < 10:
            time, tweetId, followeeId, index = heapq.heappop(min_heap)
            res.append(tweetId)
            if index >= 0:
                next_time, next_tweet = self.tweets[followeeId][index]
                heapq.heappush(min_heap, (next_time, next_tweet, followeeId, index - 1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
