class Twitter:

    def __init__(self):
        self.followerMap = {}
        self.tweets = {}
        self.tweetCount = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.tweets:
            self.tweets[userId].append([-self.tweetCount, tweetId])
        else:
            self.tweets[userId] = [[-self.tweetCount, tweetId]]
        self.tweetCount += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        followed = self.followerMap[userId].copy() if userId in self.followerMap else set()
        followed.add(userId)
        heap = []
        res = []
        for userId in followed:
            if userId in self.tweets and self.tweets[userId]:
                heapq.heappush(heap, self.tweets[userId][len(self.tweets[userId]) - 1])
        index = 2
        while heap and len(res) < 10:
            for userId in followed:
                if userId in self.tweets:
                    tweetCol = self.tweets[userId]
                    if len(tweetCol) - index >= 0:
                        heapq.heappush(heap, tweetCol[len(tweetCol) - index])
            print(heap)
            top = heapq.heappop(heap)
            res.append(top[1])
            index += 1
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followerMap:
            self.followerMap[followerId] = set()
            self.followerMap[followerId].add(followeeId)
        else:
            self.followerMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        while followeeId in self.followerMap[followerId]:
            self.followerMap[followerId].discard(followeeId)
